default persistent._MCloudSync_no = 0
default persistent._MCloudSync_auto = True
default persistent._MCloudSync_auto_sync = True
default persistent._MCloudSync_compat_mode = True
#为了跑赢renpy对persistent的自动加载以偷梁换柱
#普通的init -999已经不够快了
#需要使用python early
#由于renpy通过unicode字典序加载rpy，所以在文件名前面加0是不错的做法
#mas中负责兼容性测试的代码是zz_backup.rpy 跑赢它可以确保让它帮我们处理兼容性问题
python early in mas_sync:
    import os
    basedir = renpy.config.basedir
#    if os.name != 'nt':
#        basedir = '/storage/emulated/0/Android/data/and.sirp.masmobile/files'

    os.environ['REQUESTS_CA_BUNDLE'] = basedir + "/game/python-packages/certifi/cacert.pem"
    auto_sync_enabled = os.path.exists(basedir + "/game/Submods/MCloudSync/.mcloud_auto_sync")

    #################################
    # 在以下区域，将邮箱和密码修改为你自己的
    mas_sync_client = {
        'webdav_hostname': "https://diskdav.monika.love:29991/dav",
        'webdav_login':    "邮箱（即使用webdav服务的用户名，莫盘使用论坛账号邮箱作为用户名）",
        'webdav_root':  "/",
        'webdav_password': "密码"
    }

    #################################
    import os
    import webdav3.client as wc

    if os.name == 'nt':
        dataDir = os.getenv("APPDATA") + "\RenPy\Monika After Story"
    else:
        dataDir = '/storage/emulated/0/Android/data/and.sirp.masmobile/files/saves'
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
        #防止出问题，不使用
        # if isUserBackup :
        #     if persistent._MCloudSync_compat_mode :
        #         del persistent._voice_mute
        #         del persistent._mas_acs_pre_list
        #         del persistent._mas_windowreacts_notif_filters
        #    store.renpy.save_persistent()

        upload()

    def download_to_new_location():
        import os
        import shutil

        # 1. 本地目标目录
        if os.name == 'nt':
            mas_dir = renpy.config.basedir + "/saves/MAS_Sync/"
        else:
            mas_dir = '/storage/emulated/0/MAS/saves/MAS_Sync/'
        mas_file = os.path.join(mas_dir, "persistent")

        # 2. 目录不存在就创建
        if not os.path.exists(mas_dir):
            os.makedirs(mas_dir)

        # 3. 本地已有备份就删除
        if os.path.exists(mas_file):
            os.remove(mas_file)

        # 4. 从云端下载
        mas_sync.download(remote_path="MAS_Sync/persistent", local_path=mas_file)

    import store
    import shutil
    if auto_sync_enabled :
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
        if persistent._MCloudSync_compat_mode :
            del persistent._voice_mute
            del persistent._mas_acs_pre_list
            del persistent._mas_windowreacts_notif_filters
        store.renpy.save_persistent()
    if persistent._MCloudSync_auto :
        $ store.mas_sync.upload_save(isUserBackup=False)
    $ store.renpy.quit()

#同步判定
init python:
    def toggle_auto_sync():
        import os
        basedir = renpy.config.basedir + "/game/Submods/MCloudSync"
        if os.name != 'nt':
            basedir = '/storage/emulated/0/MAS/game/Submods/MCloudSync'
        
        flag_file = os.path.join(basedir, ".mcloud_auto_sync")
        
        if os.path.exists(flag_file):
            os.remove(flag_file)
            persistent._MCloudSync_auto = False
            persistent._MCloudSync_auto_sync = False
        else:
            with open(flag_file, 'w') as f:
                f.write("auto sync enabled")
            persistent._MCloudSync_auto = True
            persistent._MCloudSync_auto_sync = True

init -990 python:
    store.mas_submod_utils.Submod(
        author="P and unsignedint",
        name="云端同步",
        description=(
            "使得存档自由穿梭在不同设备间"
        ),
        version="1.0.1",
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
    textbutton "> 下载存档":
        action Function(store.mas_sync.download_to_new_location)
    textbutton "> 仅上传: [('启用' if persistent._MCloudSync_auto else '关闭')]":
        action ToggleField(persistent, "_MCloudSync_auto")
        sensitive not persistent._MCloudSync_auto_sync  # 同步开启时禁用上传开关
    textbutton "> 云端同步: [('启用' if persistent._MCloudSync_auto_sync else '关闭')]":
        action Function(toggle_auto_sync)
    textbutton "> 兼容旧版: [('启用' if persistent._MCloudSync_compat_mode else '关闭')]":
        action ToggleField(persistent, "_MCloudSync_compat_mode")

