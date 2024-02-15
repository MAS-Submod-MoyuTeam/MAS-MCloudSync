# -*- coding: utf-8 -*-
from ..FotoFestival import FotoFestival


class FotoUtil:
    """
    佛历工具
    """

    # 观音斋日期
    DAY_ZHAI_GUAN_YIN = ("1-8", "2-7", "2-9", "2-19", "3-3", "3-6", "3-13", "4-22", "5-3", "5-17", "6-16", "6-18", "6-19", "6-23", "7-13", "8-16", "9-19", "9-23", "10-2", "11-19", "11-24", "12-25")

    __DJ = "犯者夺纪"
    __JS = "犯者减寿"
    __SS = "犯者损寿"
    __XL = "犯者削禄夺纪"
    __JW = "犯者三年内夫妇俱亡"

    __Y = FotoFestival("杨公忌")
    __T = FotoFestival("四天王巡行", "", True)
    __D = FotoFestival("斗降", __DJ, True)
    __S = FotoFestival("月朔", __DJ, True)
    __W = FotoFestival("月望", __DJ, True)
    __H = FotoFestival("月晦", __JS, True)
    __L = FotoFestival("雷斋日", __JS, True)
    __J = FotoFestival("九毒日", "犯者夭亡，奇祸不测")
    __R = FotoFestival("人神在阴", "犯者得病", True, "宜先一日即戒")
    __M = FotoFestival("司命奏事", __JS, True, "如月小，即戒廿九")
    __HH = FotoFestival("月晦", __JS, True, "如月小，即戒廿九")

    # 日期对应的非正式节日
    FESTIVAL = {
        "1-1": [FotoFestival("天腊，玉帝校世人神气禄命", __XL), __S],
        "1-3": [FotoFestival("万神都会", __DJ), __D],
        "1-5": [FotoFestival("五虚忌")],
        "1-6": [FotoFestival("六耗忌"), __L],
        "1-7": [FotoFestival("上会日", __SS)],
        "1-8": [FotoFestival("五殿阎罗天子诞", __DJ), __T],
        "1-9": [FotoFestival("玉皇上帝诞", __DJ)],
        "1-13": [__Y],
        "1-14": [FotoFestival("三元降", __JS), __T],
        "1-15": [FotoFestival("三元降", __JS), FotoFestival("上元神会", __DJ), __W, __T],
        "1-16": [FotoFestival("三元降", __JS)],
        "1-19": [FotoFestival("长春真人诞")],
        "1-23": [FotoFestival("三尸神奏事"), __T],
        "1-25": [__H, FotoFestival("天地仓开日", "犯者损寿，子带疾")],
        "1-27": [__D],
        "1-28": [__R],
        "1-29": [__T],
        "1-30": [__HH, __M, __T],
        "2-1": [FotoFestival("一殿秦广王诞", __DJ), __S],
        "2-2": [FotoFestival("万神都会", __DJ), FotoFestival("福德土地正神诞", "犯者得祸")],
        "2-3": [FotoFestival("文昌帝君诞", __XL), __D],
        "2-6": [FotoFestival("东华帝君诞"), __L],
        "2-8": [FotoFestival("释迦牟尼佛出家", __DJ), FotoFestival("三殿宋帝王诞", __DJ), FotoFestival("张大帝诞", __DJ), __T],
        "2-11": [__Y],
        "2-14": [__T],
        "2-15": [FotoFestival("释迦牟尼佛涅槃", __XL), FotoFestival("太上老君诞", __XL), FotoFestival("月望", __XL, True), __T],
        "2-17": [FotoFestival("东方杜将军诞")],
        "2-18": [FotoFestival("四殿五官王诞", __XL), FotoFestival("至圣先师孔子讳辰", __XL)],
        "2-19": [FotoFestival("观音大士诞", __DJ)],
        "2-21": [FotoFestival("普贤菩萨诞")],
        "2-23": [__T],
        "2-25": [__H],
        "2-27": [__D],
        "2-28": [__R],
        "2-29": [__T],
        "2-30": [__HH, __M, __T],
        "3-1": [FotoFestival("二殿楚江王诞", __DJ), __S],
        "3-3": [FotoFestival("玄天上帝诞", __DJ), __D],
        "3-6": [__L],
        "3-8": [FotoFestival("六殿卞城王诞", __DJ), __T],
        "3-9": [FotoFestival("牛鬼神出", "犯者产恶胎"), __Y],
        "3-12": [FotoFestival("中央五道诞")],
        "3-14": [__T],
        "3-15": [FotoFestival("昊天上帝诞", __DJ), FotoFestival("玄坛诞", __DJ), __W, __T],
        "3-16": [FotoFestival("准提菩萨诞", __DJ)],
        "3-19": [FotoFestival("中岳大帝诞"), FotoFestival("后土娘娘诞"), FotoFestival("三茅降")],
        "3-20": [FotoFestival("天地仓开日", __SS), FotoFestival("子孙娘娘诞")],
        "3-23": [__T],
        "3-25": [__H],
        "3-27": [FotoFestival("七殿泰山王诞"), __D],
        "3-28": [__R, FotoFestival("苍颉至圣先师诞", __XL), FotoFestival("东岳大帝诞")],
        "3-29": [__T],
        "3-30": [__HH, __M, __T],
        "4-1": [FotoFestival("八殿都市王诞", __DJ), __S],
        "4-3": [__D],
        "4-4": [FotoFestival("万神善会", "犯者失瘼夭胎"), FotoFestival("文殊菩萨诞")],
        "4-6": [__L],
        "4-7": [FotoFestival("南斗、北斗、西斗同降", __JS), __Y],
        "4-8": [FotoFestival("释迦牟尼佛诞", __DJ), FotoFestival("万神善会", "犯者失瘼夭胎"), FotoFestival("善恶童子降", "犯者血死"), FotoFestival("九殿平等王诞"), __T],
        "4-14": [FotoFestival("纯阳祖师诞", __JS), __T],
        "4-15": [__W, FotoFestival("钟离祖师诞"), __T],
        "4-16": [FotoFestival("天地仓开日", __SS)],
        "4-17": [FotoFestival("十殿转轮王诞", __DJ)],
        "4-18": [FotoFestival("天地仓开日", __SS), FotoFestival("紫徽大帝诞", __SS)],
        "4-20": [FotoFestival("眼光圣母诞")],
        "4-23": [__T],
        "4-25": [__H],
        "4-27": [__D],
        "4-28": [__R],
        "4-29": [__T],
        "4-30": [__HH, __M, __T],
        "5-1": [FotoFestival("南极长生大帝诞", __DJ), __S],
        "5-3": [__D],
        "5-5": [FotoFestival("地腊", __XL), FotoFestival("五帝校定生人官爵", __XL), __J, __Y],
        "5-6": [__J, __L],
        "5-7": [__J],
        "5-8": [FotoFestival("南方五道诞"), __T],
        "5-11": [FotoFestival("天地仓开日", __SS), FotoFestival("天下都城隍诞")],
        "5-12": [FotoFestival("炳灵公诞")],
        "5-13": [FotoFestival("关圣降", __XL)],
        "5-14": [FotoFestival("夜子时为天地交泰", __JW), __T],
        "5-15": [__W, __J, __T],
        "5-16": [FotoFestival("九毒日", __JW), FotoFestival("天地元气造化万物之辰", __JW)],
        "5-17": [__J],
        "5-18": [FotoFestival("张天师诞")],
        "5-22": [FotoFestival("孝娥神诞", __DJ)],
        "5-23": [__T],
        "5-25": [__J, __H],
        "5-26": [__J],
        "5-27": [__J, __D],
        "5-28": [__R],
        "5-29": [__T],
        "5-30": [__HH, __M, __T],
        "6-1": [__S],
        "6-3": [FotoFestival("韦驮菩萨圣诞"), __D, __Y],
        "6-5": [FotoFestival("南赡部洲转大轮", __SS)],
        "6-6": [FotoFestival("天地仓开日", __SS), __L],
        "6-8": [__T],
        "6-10": [FotoFestival("金粟如来诞")],
        "6-14": [__T],
        "6-15": [__W, __T],
        "6-19": [FotoFestival("观世音菩萨成道", __DJ)],
        "6-23": [FotoFestival("南方火神诞", "犯者遭回禄"), __T],
        "6-24": [FotoFestival("雷祖诞", __XL), FotoFestival("关帝诞", __XL)],
        "6-25": [__H],
        "6-27": [__D],
        "6-28": [__R],
        "6-29": [__T],
        "6-30": [__HH, __M, __T],
        "7-1": [__S, __Y],
        "7-3": [__D],
        "7-5": [FotoFestival("中会日", __SS, False, "一作初七")],
        "7-6": [__L],
        "7-7": [FotoFestival("道德腊", __XL), FotoFestival("五帝校生人善恶", __XL), FotoFestival("魁星诞", __XL)],
        "7-8": [__T],
        "7-10": [FotoFestival("阴毒日", "", False, "大忌")],
        "7-12": [FotoFestival("长真谭真人诞")],
        "7-13": [FotoFestival("大势至菩萨诞", __JS)],
        "7-14": [FotoFestival("三元降", __JS), __T],
        "7-15": [__W, FotoFestival("三元降", __DJ), FotoFestival("地官校籍", __DJ), __T],
        "7-16": [FotoFestival("三元降", __JS)],
        "7-18": [FotoFestival("西王母诞", __DJ)],
        "7-19": [FotoFestival("太岁诞", __DJ)],
        "7-22": [FotoFestival("增福财神诞", __XL)],
        "7-23": [__T],
        "7-25": [__H],
        "7-27": [__D],
        "7-28": [__R],
        "7-29": [__Y, __T],
        "7-30": [FotoFestival("地藏菩萨诞", __DJ), __HH, __M, __T],
        "8-1": [__S, FotoFestival("许真君诞")],
        "8-3": [__D, FotoFestival("北斗诞", __XL), FotoFestival("司命灶君诞", "犯者遭回禄")],
        "8-5": [FotoFestival("雷声大帝诞", __DJ)],
        "8-6": [__L],
        "8-8": [__T],
        "8-10": [FotoFestival("北斗大帝诞")],
        "8-12": [FotoFestival("西方五道诞")],
        "8-14": [__T],
        "8-15": [__W, FotoFestival("太明朝元", "犯者暴亡", False, "宜焚香守夜"), __T],
        "8-16": [FotoFestival("天曹掠刷真君降", "犯者贫夭")],
        "8-18": [FotoFestival("天人兴福之辰", "", False, "宜斋戒，存想吉事")],
        "8-23": [FotoFestival("汉恒候张显王诞"), __T],
        "8-24": [FotoFestival("灶君夫人诞")],
        "8-25": [__H],
        "8-27": [__D, FotoFestival("至圣先师孔子诞", __XL), __Y],
        "8-28": [__R, FotoFestival("四天会事")],
        "8-29": [__T],
        "8-30": [FotoFestival("诸神考校", "犯者夺算"), __HH, __M, __T],
        "9-1": [__S, FotoFestival("南斗诞", __XL), FotoFestival("北斗九星降世", __DJ, False, "此九日俱宜斋戒")],
        "9-3": [__D, FotoFestival("五瘟神诞")],
        "9-6": [__L],
        "9-8": [__T],
        "9-9": [FotoFestival("斗母诞", __XL), FotoFestival("酆都大帝诞"), FotoFestival("玄天上帝飞升")],
        "9-10": [FotoFestival("斗母降", __DJ)],
        "9-11": [FotoFestival("宜戒")],
        "9-13": [FotoFestival("孟婆尊神诞")],
        "9-14": [__T],
        "9-15": [__W, __T],
        "9-17": [FotoFestival("金龙四大王诞", "犯者遭水厄")],
        "9-19": [FotoFestival("日宫月宫会合", __JS), FotoFestival("观世音菩萨诞", __JS)],
        "9-23": [__T],
        "9-25": [__H, __Y],
        "9-27": [__D],
        "9-28": [__R],
        "9-29": [__T],
        "9-30": [FotoFestival("药师琉璃光佛诞", "犯者危疾"), __HH, __M, __T],
        "10-1": [__S, FotoFestival("民岁腊", __DJ), FotoFestival("四天王降", "犯者一年内死")],
        "10-3": [__D, FotoFestival("三茅诞")],
        "10-5": [FotoFestival("下会日", __JS), FotoFestival("达摩祖师诞", __JS)],
        "10-6": [__L, FotoFestival("天曹考察", __DJ)],
        "10-8": [FotoFestival("佛涅槃日", "", False, "大忌色欲"), __T],
        "10-10": [FotoFestival("四天王降", "犯者一年内死")],
        "10-11": [FotoFestival("宜戒")],
        "10-14": [FotoFestival("三元降", __JS), __T],
        "10-15": [__W, FotoFestival("三元降", __DJ), FotoFestival("下元水府校籍", __DJ), __T],
        "10-16": [FotoFestival("三元降", __JS), __T],
        "10-23": [__Y, __T],
        "10-25": [__H],
        "10-27": [__D, FotoFestival("北极紫徽大帝降")],
        "10-28": [__R],
        "10-29": [__T],
        "10-30": [__HH, __M, __T],
        "11-1": [__S],
        "11-3": [__D],
        "11-4": [FotoFestival("至圣先师孔子诞", __XL)],
        "11-6": [FotoFestival("西岳大帝诞")],
        "11-8": [__T],
        "11-11": [FotoFestival("天地仓开日", __DJ), FotoFestival("太乙救苦天尊诞", __DJ)],
        "11-14": [__T],
        "11-15": [FotoFestival("月望", "上半夜犯男死 下半夜犯女死"), FotoFestival("四天王巡行", "上半夜犯男死 下半夜犯女死")],
        "11-17": [FotoFestival("阿弥陀佛诞")],
        "11-19": [FotoFestival("太阳日宫诞", "犯者得奇祸")],
        "11-21": [__Y],
        "11-23": [FotoFestival("张仙诞", "犯者绝嗣"), __T],
        "11-25": [FotoFestival("掠刷大夫降", "犯者遭大凶"), __H],
        "11-26": [FotoFestival("北方五道诞")],
        "11-27": [__D],
        "11-28": [__R],
        "11-29": [__T],
        "11-30": [__HH, __M, __T],
        "12-1": [__S],
        "12-3": [__D],
        "12-6": [FotoFestival("天地仓开日", __JS), __L],
        "12-7": [FotoFestival("掠刷大夫降", "犯者得恶疾")],
        "12-8": [FotoFestival("王侯腊", __DJ), FotoFestival("释迦如来成佛之辰"), __T, FotoFestival("初旬内戊日，亦名王侯腊", __DJ)],
        "12-12": [FotoFestival("太素三元君朝真")],
        "12-14": [__T],
        "12-15": [__W, __T],
        "12-16": [FotoFestival("南岳大帝诞")],
        "12-19": [__Y],
        "12-20": [FotoFestival("天地交道", "犯者促寿")],
        "12-21": [FotoFestival("天猷上帝诞")],
        "12-23": [FotoFestival("五岳诞降"), __T],
        "12-24": [FotoFestival("司今朝天奏人善恶", "犯者得大祸")],
        "12-25": [FotoFestival("三清玉帝同降，考察善恶", "犯者得奇祸"), __H],
        "12-27": [__D],
        "12-28": [__R],
        "12-29": [FotoFestival("华严菩萨诞"), __T],
        "12-30": [FotoFestival("诸神下降，察访善恶", "犯者男女俱亡")]
    }

    def __init__(self):
        pass
