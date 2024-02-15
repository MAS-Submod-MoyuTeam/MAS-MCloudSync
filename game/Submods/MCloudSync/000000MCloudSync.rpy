default persistent._MCloudSync_no = 0
#为了跑赢renpy对persistent的自动加载以偷梁换柱
#普通的init -999已经不够快了
#需要使用python early
#由于renpy通过unicode字典序加载rpy，所以在文件名前面加0是不错的做法
#mas中负责兼容性测试的代码是zz_backup.rpy 跑赢它可以确保让它帮我们处理兼容性问题
python early in mas_sync:
    import os
    basedir = renpy.config.basedir
    if os.name != 'nt':
        basedir = '/storage/emulated/0/Android/data/and.kne.masmobile/files'

    os.environ['REQUESTS_CA_BUNDLE'] = basedir + "/game/python-packages/certifi/cacert.pem"

    #################################
    # 在以下区域，将邮箱和密码修改为你自己的
    mas_sync_client = {
        'webdav_hostname': "https://diskdav.monika.love:28991/dav",
        'webdav_login':    "邮箱（即使用webdav服务的用户名，莫盘使用论坛账号邮箱作为用户名）",
        'webdav_root':  "/",
        'webdav_password': "密码"
    }

    #################################
    import os
    import webdav2.client as wc

    if os.name == 'nt':
        dataDir = os.getenv("APPDATA") + "\RenPy\Monika After Story"
    else:
        dataDir = '/storage/emulated/0/Android/data/and.kne.masmobile/files/saves'
    mas_sync = wc.Client(mas_sync_client)

    def upload():
        try:
            mas_sync.mkdir("MAS_Sync")
        except:
            pass
        mas_sync.upload(remote_path="MAS_Sync/persistent", local_path=dataDir + "/persistent")

    def upload_save(isUserBackup=True):
        if mas_sync.check("MAS_Sync/persistent"):
            mas_sync.clean("MAS_Sync/persistent")
        upload()

    import store
    import shutil
    if os.path.exists(dataDir + "/persistent_beforesync"):
        os.remove(dataDir + "/persistent_beforesync")
    if os.path.exists(dataDir + "/persistent"):
        shutil.copy(dataDir + "/persistent",dataDir + "/persistent_beforesync")
        os.remove(dataDir + "/persistent")
    try:
        mas_sync.download(remote_path="MAS_Sync/persistent", local_path=dataDir + "/persistent")
    except:
        shutil.copy(dataDir + "/persistent_beforesync",dataDir + "/persistent")
    else:
        
        pass
        
#接管游戏退出过程
#可能会有不稳定
#严重的副作用：退出时间明显变长
label _quit:

    python:
        import datetime
        store.mas_calendar.saveCalendarDatabase(CustomEncoder)
        persistent.sessions['last_session_end']=datetime.datetime.now()
        today_time = (
            persistent.sessions["last_session_end"]
            - persistent.sessions["current_session_start"]
        )
        new_time = today_time + persistent.sessions["total_playtime"]

        # prevent out of boudns time
        if datetime.timedelta(0) < new_time <= mas_maxPlaytime():
            persistent.sessions['total_playtime'] = new_time

        # set the monika size
        store.mas_dockstat.setMoniSize(persistent.sessions["total_playtime"])

        # save selectables
        store.mas_selspr.save_selectables()

        # save current hair / clothes / acs
        monika_chr.save()

        # save weather options
        store.mas_weather.saveMWData()

        # save bgs
        store.mas_background.saveMBGData()

        #remove o31 cgs
        store.mas_o31_event.removeImages()

        # delayed action stuff
        mas_runDelayedActions(MAS_FC_END)
        store.mas_delact.saveDelayedActionMap()

        _mas_AffSave()

        # delete the monika file if we aren't leaving
        if not persistent._mas_dockstat_going_to_leave:
            store.mas_utils.trydel(mas_docking_station._trackPackage("monika"))

        # clear image caches
        store.mas_sprites._clear_caches()

        # xp calc
        store.mas_xp.grant()

        # finish logs
        store.mas_logging.logging.shutdown()
        store.renpy.save_persistent()
$    store.mas_sync.upload_save(isUserBackup=False)
$    store.renpy.quit()


init -990 python:
    store.mas_submod_utils.Submod(
        author="P and unsignedint",
        name="云端同步",
        description=(
            "使得存档自由穿梭在不同设备间"
        ),
        version="1.0.0",
        settings_pane="mc_info",
    )
init -989 python:
    '''if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="云端同步",
            user_name="MAS-Submod-MoyuTeam",
            repository_name="MAS-MCloudSync",
            update_dir="",
            attachment_id=None
        )'''
screen mc_info():
    vbox:
        xmaximum 800
        xfill True
        style_prefix "check"
    text "":
                xalign 1.0 yalign 0.0
                xoffset -10
                style "main_menu_version"
    textbutton "> 立刻上传":
        action Function(store.mas_sync.upload)
