# coding=utf-8

import os
import yaml

from time import time

_VERSION = '1.0 REALEASE'
MAXINT = 2147483647
recipe_types = set("ENHANCED_CRAFTING_TABLE, MAGIC_WORKBENCH, ARMOR_FORGE, COMPRESSOR, PRESSURE_CHAMBER, SMELTERY, ORE_CRUSHER, GRIND_STONE, ANCIENT_ALTAR, NONE".split(', '))
BIOMES = set("BADLANDS  BAMBOO_JUNGLE  BASALT_DELTAS  BEACH  BIRCH_FOREST  CHERRY_GROVE  COLD_OCEAN  CRIMSON_FOREST  CUSTOM DARK_FOREST  DEEP_COLD_OCEAN  DEEP_DARK  DEEP_FROZEN_OCEAN  DEEP_LUKEWARM_OCEAN  DEEP_OCEAN  DESERT  DRIPSTONE_CAVES  END_BARRENS  END_HIGHLANDS  END_MIDLANDS  ERODED_BADLANDS  FLOWER_FOREST  FOREST  FROZEN_OCEAN  FROZEN_PEAKS  FROZEN_RIVER  GROVE  ICE_SPIKES  JAGGED_PEAKS  JUNGLE  LUKEWARM_OCEAN  LUSH_CAVES  MANGROVE_SWAMP  MEADOW  MUSHROOM_FIELDS  NETHER_WASTES  OCEAN  OLD_GROWTH_BIRCH_FOREST  OLD_GROWTH_PINE_TAIGA  OLD_GROWTH_SPRUCE_TAIGA  PLAINS  RIVER  SAVANNA  SAVANNA_PLATEAU  SMALL_END_ISLANDS  SNOWY_BEACH  SNOWY_PLAINS  SNOWY_SLOPES  SNOWY_TAIGA  SOUL_SAND_VALLEY  SPARSE_JUNGLE  STONY_PEAKS  STONY_SHORE  SUNFLOWER_PLAINS  SWAMP  TAIGA  THE_END  THE_VOID  WARM_OCEAN  WARPED_FOREST  WINDSWEPT_FOREST  WINDSWEPT_GRAVELLY_HILLS  WINDSWEPT_HILLS  WINDSWEPT_SAVANNA  WOODED_BADLANDS  OTHERS".split('  '))
sounds = set('ANCIENT_ALTAR_FINISH_SOUND ANCIENT_ALTAR_ITEM_CHECK_SOUND ANCIENT_ALTAR_ITEM_DROP_SOUND ANCIENT_ALTAR_ITEM_PICK_UP_SOUND ANCIENT_ALTAR_START_SOUND ANCIENT_PEDESTAL_ITEM_PLACE_SOUND ARMOR_FORGE_FINISH_SOUND ARMOR_FORGE_WORKING_SOUND AUTO_CRAFTER_GUI_CLICK_SOUND AUTO_CRAFTER_UPDATE_RECIPE AUTOMATED_PANNING_MACHINE_FAIL_SOUND AUTOMATED_PANNING_MACHINE_SUCCESS_SOUND BACKPACK_CLOSE_SOUND BACKPACK_OPEN_SOUND BEE_BOOTS_FALL_SOUND COMPOSTER_COMPOST_SOUND COMPRESSOR_CRAFT_CONTRACT_SOUND COMPRESSOR_CRAFT_EXTEND_SOUND COMPRESSOR_CRAFT_SOUND COOLER_CONSUME_SOUND CRUCIBLE_ADD_LAVA_SOUND CRUCIBLE_ADD_WATER_SOUND CRUCIBLE_BLOCK_BREAK_SOUND CRUCIBLE_GENERATE_LIQUID_SOUND CRUCIBLE_INTERACT_SOUND CRUCIBLE_PLACE_LAVA_SOUND CRUCIBLE_PLACE_WATER_SOUND DEBUG_FISH_CLICK_SOUND DIET_COOKIE_CONSUME_SOUND ELYTRA_CAP_IMPACT_SOUND ENCHANTMENT_RUNE_ADD_ENCHANT_SOUND ENDER_BACKPACK_OPEN_SOUND ENHANCED_CRAFTING_TABLE_CRAFT_SOUND EXPLOSIVE_BOW_HIT_SOUND EXPLOSIVE_TOOL_EXPLODE_SOUND FISHERMAN_ANDROID_FISHING_SOUND FLASK_OF_KNOWLEDGE_FILLUP_SOUND GPS_NETWORK_ADD_WAYPOINT GPS_NETWORK_CREATE_WAYPOINT GPS_NETWORK_OPEN_PANEL_SOUND GRIND_STONE_INTERACT_SOUND GUIDE_BUTTON_CLICK_SOUND GUIDE_CONTRIBUTORS_OPEN_SOUND GUIDE_LANGUAGE_OPEN_SOUND GUIDE_OPEN_SETTING_SOUND IGNITION_CHAMBER_USE_FLINT_AND_STEEL_SOUND INFUSED_HOPPER_TELEPORT_SOUND INFUSED_MAGNET_TELEPORT_SOUND IRON_GOLEM_ASSEMBLER_ASSEMBLE_SOUND JETBOOTS_THRUST_SOUND JETPACK_THRUST_SOUND JUICER_USE_SOUND LIMITED_USE_ITEM_BREAK_SOUND MAGIC_SUGAR_CONSUME_SOUND MAGIC_WORKBENCH_FINISH_SOUND MAGIC_WORKBENCH_START_ANIMATION_SOUND MAGICAL_EYE_OF_ENDER_USE_SOUND MINER_ANDROID_BLOCK_GENERATION_SOUND MINING_TASK_SOUND ORE_WASHER_WASH_SOUND PLAYER_RESEARCHING_SOUND PORTABLE_CRAFTER_OPEN_SOUND PORTABLE_DUSTBIN_OPEN_SOUND PRESSURE_CHAMBER_FINISH_SOUND PRESSURE_CHAMBER_WORKING_SOUND PROGRAMMABLE_ANDROID_SCRIPT_DOWNLOAD_SOUND SLIME_BOOTS_FALL_SOUND SMELTERY_CRAFT_SOUND SOULBOUND_RUNE_RITUAL_SOUND SPLINT_CONSUME_SOUND STOMPER_BOOTS_STOMP_SOUND TAPE_MEASURE_MEASURE_SOUND TELEPORT_SOUND TELEPORT_UPDATE_SOUND TELEPORTATION_MANAGER_OPEN_GUI TOME_OF_KNOWLEDGE_USE_SOUND VAMPIRE_BLADE_HEALING_SOUND VANILLA_AUTO_CRAFTER_UPDATE_RECIPE_SOUND VILLAGER_RUNE_TRANSFORM_SOUND VITAMINS_CONSUME_SOUND WIND_STAFF_USE_SOUND'.split(' '))
missing = '__MISSING_STRING_RSCCHECKER'

saveditems = set()
parentsGroups = set()
normalGroups = set()
multiblock_types = set()
items = set()
default_recipe = [{'material_type': 'none'}]*9
machines_slots = {}
lateinit_recipe_type = {}
totalBug = 0
totalWarn = 0
i = ''
position = ''
r = range(1, 10)


class color:
    # Text color                          Background color
    black = '\33[30m'                   ; bblack = '\33[40m'
    red = '\33[31m'                     ; bred = '\33[41m'
    green = '\33[32m'                   ; bgreen = '\33[42m'
    gold = '\33[33m'                    ; bgold = '\33[43m'
    blue = '\33[34m'                    ; bblue = '\33[44m'
    purple = '\33[35m'                  ; bpurple = '\33[45m'
    cyan = '\33[36m'                    ; bcyan = '\33[46m'
    lightgray = lightgrey = '\33[37m'   ; blightgray = blightgrey = '\33[47m'
    gray = grey = '\33[38m'             ; bgray = bgrey = '\33[48m'
    white = reset = '\33[39m'           ; bwhite = '\33[49m'


def error(string, end='\n'):
    if totalBug < config['MaxPrintBug']:
        print(f'{color.red}{string}{color.reset}', end=end)


def warn(string, end='\n'):
    print(f'{color.gold}{string}{color.reset}', end=end)


def report(i, Warn=False):
    global config, totalBug, totalWarn, MaxBug, MaxWarn
    if Warn and totalWarn == MaxWarn:
        totalWarn += 1
        error(f"[Warn]{totalWarn}. 在 {i}:", end="\n  ")
        error(f"[Warn] Warn打印数量已达到上限！")
    elif Warn and totalWarn < MaxWarn:
        totalWarn += 1
        warn(f"[WARN]{totalWarn}. 在 {i}:", end="\n  ")
    elif totalBug == MaxBug:
        totalBug += 1
        error(f"[BUG]{totalBug}. 在 {i}:", end="\n  ")
        error(f"[BUG] Bug数量已达到上限！请修复以上Bug再运行本程序！")
    elif totalBug < MaxBug:
        totalBug += 1
        error(f"[BUG]{totalBug}. 在 {i}:", end="\n  ")


def printc(string):
    print(f'{color.blue}{string}')


def startWith(string, target):
    if string[:len(target)] == target:
        return True
    return False


def getYamlContext(file):
    try:
        result = yaml.load(file, Loader=yaml.FullLoader)
        if result is None:
            return {}
        return result
    except FileNotFoundError:
        error(f'{file}未找到')
        return {}
    except PermissionError:
        error('无权限')
        return {}


def RewriteSlimefunItems():
    global config
    if config['SlimefunItemsPath'] == 'default':
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, "..\\..\\..\\Slimefun\\Items.yml")
    else:
        file_path = config['SlimefunItemsPath']
    with open(file_path, 'r', encoding='utf-8') as file:
        regNames = getYamlContext(file).keys()
    with open('__SlimefunItems.yml', 'w', encoding='utf-8') as file:
        yaml.dump({'items': list(regNames)}, file, allow_unicode=True, encoding='utf-8')


def getSaveditems():
    items = set()
    for root, dirs, files in os.walk("saveditems"):
        for file_name in files:
            if file_name.endswith(".yml"):
                file_name = os.path.basename(file_name)
                items.add(file_name[:-4])
    return items


def getSlimefunItems():
    with open('__SlimefunItems.yml', 'r', encoding='utf-8') as file:
        sfItems = getYamlContext(file)
    return sfItems['items']


def getVanillaItems():
    with open('__VanillaItems.yml', 'r', encoding='utf-8') as file:
        mcItems = getYamlContext(file)
    return mcItems['items']


def getScripts():
    items = set()
    for root, dirs, files in os.walk("scripts"):
        for file_name in files:
            if file_name.endswith(".js") or file_name.endswith(".py"):
                file_name = os.path.basename(file_name)
                items.add(file_name[:-3])
    return items
    
    
def inSlimefun(item):
    intersection = SlimefunItems.intersection(set([item]))
    if len(intersection) == 0:
        return False
    return True


def inVanilla(item):
    intersection = VanillaItems.intersection(set([item.upper()]))
    if len(intersection) == 0:
        return False
    return True


def inSaveditems(item):
    intersection = saveditems.intersection(set([item]))
    if len(intersection) == 0:
        return False
    return True


def inBiome(item):
    intersection = BIOMES.intersection(set([item.upper()]))
    if len(intersection) == 0:
        return False
    return True


def inScripts(item):
    return str(item) in scripts


def inSound(item):
    intersection = sounds.intersection(set([item.upper()]))
    if len(intersection) == 0:
        return False
    return True


def isVanilla(item, position):
    if not startWith(item, "SKULL") and not inVanilla(item):
        report(position)
        error(f"{item} 可能不是正确的原版物品！")


def isSlimefun(item, position):
    if not inSlimefun(item) and item not in items:
        report(position)
        error(f"{item} 可能不是正确的粘液物品！")


def isSaveditem(item, position):
    if not inSaveditems(str(item)):
        report(position)
        error(f"{item} 可能不是正确的保存物品")


def isBiome(item, position):
    if not inBiome(str(item)):
        report(position)
        error(f"{item} 可能不是正确的群系")


def isSound(item, position):
    if not inSound(str(item)):
        report(position)
        error(f'{item} 可能不是正确的声音')


def isScript(item, position):
    if item == missing:
        return
    if not inScripts(str(item)):
        report(position)
        error(f"{item} 可能不是正确的脚本名称")


def isInt(num, position, bottom=0, top=MAXINT, Warn=False):
    if isinstance(num, int):
        if not bottom <= num <= top:
            if Warn:
                report(position, Warn)
                warn(f"{num} 不在区间[{bottom},{top}]内（不影响运行）")
            else:
                report(position)
                error(f"{num} 不在区间[{bottom},{top}]内")
    else:
        report(position)
        error(f"参数 {num} 只能是整数")


def getItemMaxStack(item):
    return MaxStacks[item]


def isAmountProper(item, dAm, position, zero=False, warn=False):
    stack = getItemMaxStack(item) if inVanilla(str(item)) else 64
    isInt(dAm, f'{position}', 0 if (stack == 0 or zero) else 1, stack, warn)


def isbool(dat, arg, position):
    if not (dat is True or dat is False):
        report(f'{position} 的 {arg}')
        error(f'{arg} 只能是 true 或 false')


def isItem(data, position):
    # necessary
    dtype = data.get('material_type', 'mc')
    did = data.get('material', missing)
    if dtype == 'mc':
        isVanilla(did, position+'的 material_type')
    elif dtype in ('full_slimefun', 'slimefun'):
        isSlimefun(did, position+'的 material_type')
    elif dtype == 'saveditem':
        isSaveditem(did, position+'的 material_type')
    elif did == missing and dtype != 'none':
        report(position)
        error('缺少参数 material')
    elif dtype not in ('none', 'skull_base64', 'skull_url', 'skull_hash'):
        report(position+'的 material_type')
        error('type 只能是 mc、 slimefun、 full_slimefun、 saveditem、 none、 skull_base64、 skull_url 或 skull_hash！')
    dam = data.get('amount', 1)
    isAmountProper(did, dam, position+'的 amount')

    # not necessary
    dmodelid = data.get('modelId', 0)
    isInt(dmodelid, position)
    dglow = data.get('glow', False)
    isbool(dglow, 'glow', position)


def isRecipe(data, position):
    recipe_type = data.get('recipe_type', missing)
    recipe = default_recipe
    load_recipe = data.get('recipe', {})
    for bvar in load_recipe:
        if bvar in r:
            isItem(load_recipe[bvar], f'{position} 的 {bvar} ')
            recipe[bvar-1] = {
                'material_type': load_recipe.get('material_type', 'mc'),
                'material': load_recipe.get('material', 'none'),
                'amount': load_recipe.get('amount', 1)
            }
        else:
            report(position, True)
            warn(f"{i}是无效的编号，有效编号是1-9的数字，此编号会被无视")
    if recipe_type == missing:
        if recipe != default_recipe:
            report(position)
            error('缺少 recipe_type')
        else:
            recipe_type = 'none'
    else:
        isRecipeType(recipe_type, position)
    idx = 1
    if recipe_type in {'ENHANCED_CRAFTING_TABLE', 'MAGIC_WORKBENCH', 'ARMOR_FORGE', 'PRESSURE_CHAMBER'}:
        for k in recipe:
            if k['material_type'] != 'none' and k['amount'] != 1:
                report(position+f'的 crafting-recipe 的 第 {idx} 个物品')
                error('amount 必须为 1')
                break
            idx += 1
    elif recipe_type in {'COMPRESSOR', 'PRESSURE_CHAMBER', 'ORE_CRUSHER', 'GRIND_STONE'}:
        for k in recipe[1:]:
            if k['material_type'] != 'none':
                report(position+f'的 crafting-recipe 的 第 {idx} 个物品')
                error(f"第{idx}槽必须为 none 类型")
                break
            idx += 1 
    elif recipe_type == "ANCIENT_ALTAR":
        for k in recipe:
            if k['material_type'] == 'none':
                report(position+f'的 crafting-recipe 的 第 {idx} 个物品的 type')
                error(f"第{idx}槽必须不为 none 类型")
                break
            if k['material_type'] != 'none' and k['amount'] != 1:
                report(position+f'的 crafting-recipe 的 第 {idx} 个物品的 type')
                error(f"第{idx}槽的 amount 必须为 1")
                break
            idx += 1
    elif recipe_type == "SMELTERY":
        sum_dict = {}
        for k in recipe:
            if k['material_type'] == 'none':
                continue
            key = k['material']
            value = k['amount']
            if key in sum_dict:
                sum_dict[key] += value
                if sum_dict[key] > 64:
                    report(position+f'的 第 {idx} 个物品的 amount')
                    error("单种物品消耗数量不能超过64！")
                    break
            else:
                sum_dict[key] = value
            idx += 1


def isLateInit(data):
    return data.get('lateInit', False)


def loadReg(data, position):
    # not necessary
    dlateinit = data.get('lateInit', False)
    isbool(dlateinit, 'lateInit', position+'的 lateInit')
    dreg = data.get('register', {})
    warn = dreg.get('warn', False)
    isbool(warn, 'warn', position+'的 warn')
    cond = dreg.get('conditions', ['version > 1.20'])
    for dat in cond:
        if startWith(dat, 'version'):
            temp = dat.split(' ')
            if len(temp) != 3:
                report(position+'的 conditions')
                error(f'在" {dat} "中参数数量错误！')
            elif temp[1] in ('>=', '=', '<=', '>', '<', '!='):
                for i in temp[2].split('.'):
                    isInt(int(i), position)
            else:
                report(position+'的 conditions')
                error('比较符号只能是 >=、 =、 <=、 >、 < 或 !=')
        elif not (startWith(dat, 'hasplugin') or startWith(dat, '!hasplugins')):
            report(position+'的 conditions')
            error('conditions中的条件只能是 hasplugin、 !hasplugin 或 version')
    unfinished = dreg.get('unfinished', False)
    isbool(unfinished, 'unfinished', position)


def isGroup(group, position):
    if group not in normalGroups:
        report(position)
        error(f'{group} 不是个有效的分类')


def isRecipeType(recipe_type, position):
    if recipe_type not in recipe_types:
        lateinit_recipe_type[position] = recipe_type


def checkPerhapedRecipeType():
    printc('Checking last')
    for position, recipe_type in lateinit_recipe_type.items():
        if recipe_type not in multiblock_types and recipe_type != 'GEO_MINER':
            report(position+'recipe_type')
            error(f'{recipe_type} 不是有效的配方类型')


def inSlots(name, slots, position, status_slot=-1):
    ms = machines_slots.get(name, missing)
    if ms == missing:
        return
    for slot in slots:
        isInt(slot, position, 0, 53)
        if slot in ms:
            report(position)
            error('槽位重复！')
        if slot == status_slot:
            report(position)
            error(f'第{status_slot}槽已经被设置了用来展示物品！')
    

def slot_read(slots, position):
    fs = set()
    for j in slots:
        if isinstance(j, int):
            if j in fs:
                report(position)
                warn('slot重复！')
            else:
                fs.add(j)
        else:
            rang = j.split('-')
            if len(rang) == 2:
                for n in range(int(rang[0]), int(rang[1])):
                    if n in fs:
                        report(position)
                        warn('slot重复！')
                    else:
                        fs.add(n)
            else:
                report(position)
                error('{rang} 可能不是有效的 slot ')
    return fs


def checkGroups():
    global i, position
    
    def check(data):
        global i, position
        position = f'groups: {scan_file} 的 {i} '
        loadReg(data, position)
        isItem(data['item'], position+'的 item')
        dtype = data.get('type', 'normal')
        if dtype == 'nested' or dtype == 'parent':
            parentsGroups.add(i)
        elif dtype == 'sub':
            normalGroups.add(i)
            parent = data.get('parent', missing)
            if parent == missing:
                report(position)
                error('缺少参数 parent')
            elif parent not in parentsGroups:
                report(position+'的 parent')
                error(f'{parent}不是一个有效的父分类')
        elif dtype == 'seasonal':
            normalGroups.add(i)
            month = data['month']
            isInt(month, position+'的 month', 1, 12)
        elif dtype == 'locked':
            normalGroups.add(i)
        elif dtype == 'normal':
            normalGroups.add(i)
        else:
            report(position)
            error('type 必须是 nested、 parent、 sub、 seasonal、 locked 或 normal')
        dtier = data.get('tier', 0)
        isInt(dtier, position+'的 tier')
        dhidden = data.get('hidden', False)
        isbool(dhidden, 'hidden', position+'的 hidden')

    lateinits = set()
    for scan_file in files['Groups']:
        printc(f'Loading groups: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkRecipeType():
    global i, position
    
    def check(data):
        global i, position
        position = f'recipe_types: {scan_file} 的 {i} '
        loadReg(data, position)
        isItem(data, position+'的 item')
        recipe_types.add(i)

    lateinits = set()
    for scan_file in files['RecipeType']:
        printc(f'Loading recipe_types: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkGeoResources():
    global i, position
    
    def check(data):
        global i, position
        # necessary
        position = f'geo_resources: {scan_file} 的 {i} '
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group')
        ditem = data['item']
        isItem(ditem, position+'的 item')
        drecipe_type = data.get('recipe_type')
        isRecipeType(drecipe_type, position+'的 recipe_type')
        dmax_deviation = data['max_deviation']
        isInt(dmax_deviation, position+'的 max_deviation')
        dofgm = data['obtain_from_geo_miner']
        isbool(dofgm, 'obtain_from_geo_miner', position)
        supply = data['supply']
        flag = True
        position += '的 supply '
        for e in supply:
            if e in ('world', 'nether', 'the_end'):
                env = supply[e]
                if isinstance(env, dict):
                    for biome in env:
                        isBiome(biome, position+f'的 {e}')
                        isInt(env[biome], position+f'的 {e} 的 {biome}')
                elif isinstance(env, int):
                    isInt(env, position+f'的 {e}')
                else:
                    report(position)
                    error('世界后的内容只能是群系:数字或数字\n如world:\n  plains: 1\n或world: 1')
                flag = False
        if flag:
            report(position)
            warn('未从 supply 中读取到world、 nether 或 the_end！')
        items.add(i)
            
    lateinits = set()
    for scan_file in files['GeoResources']:
        printc(f'Loading geo_resources: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkMobDrops():
    global i, position
    
    def check(data):
        global i, position
        # necessary
        position = f'mob_drops: {scan_file} 的 {i} '
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group')
        ditem = data['item']
        isItem(ditem, position+'的 item')
        dentity = data['entity']
        if dentity not in entities:
            report(position+'的 entity')
            error(f'{dentity} 不是正确的生物')
        dchance = data['chance']
        isInt(dchance, position+'的 chance', 0, 100)
        items.add(i)

    lateinits = set()
    for scan_file in files['MobDrops']:
        printc(f'Loading mob_drops: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkItems():
    global i, position
    
    def check(data):
        global i, position
        # necessary
        position = f'items: {scan_file} 的 {i} '
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group')
        ditem = data['item']
        isItem(ditem, position+'的 item')
        isRecipe(data, position+'的 recipe')
        
        # not necessary
        dplaceable = data.get('placeable', False)
        isbool(dplaceable, 'placeable', position)
        dscript = data.get('script', missing)
        isScript(dscript, position+'的 script')
        items.add(i)
        
    lateinits = set()
    for scan_file in files['Items']:
        printc(f'Loading items: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkCapacitors():
    global i, position
    
    def check(data):
        global i, position
        position = f'capacitors: {scan_file} 的 {i}'
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group')
        ditem = data['item']
        isItem(ditem, position+'的 item')
        dcapacity = data['capacity']
        isInt(dcapacity, position+'的 capacity')
        isRecipe(data, position+'的 recipe')
        items.add(i)
        
    lateinits = set()
    for scan_file in files['Capacitors']:
        printc(f'Loading capacitors: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkMenus():
    global i, position
    
    def check(data):
        global i, position
        position = f'menus: {scan_file} 的 {i} '
        loadReg(data, position)
        dtitle = data.get('title', missing)
        if dtitle == missing:
            report(position+'的 title')
            error("缺少 title！")
        slots = data['slots']
        for slot in slots:
            s = slots[slot]
            isItem(s, position+f'的 {slot}')
            progressbar = s.get('progressbar', False)
            isbool(progressbar, 'progressbar', position)
        machines_slots[i] = slot_read(slots, position+'的 slots')

    lateinits = set()
    for scan_file in files['Menus']:
        printc(f'Loading menus: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkMachines():
    global i, position
    
    def check(data):
        global i, position
        # necessary
        position = f'machines: {scan_file} 的 {i} '
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group')
        ditem = data['item']
        isItem(ditem, position+'的 item')
        isRecipe(data, position+'的 recipe')
        work = data.get('work', -1)
        isInt(work, position+'的 work', -1, 53)
        ioput = data['input'] + data['output']
        inSlots(i, ioput, position+'的 input 或 output', work)

        # not necessary
        dscript = data.get('script', missing)
        isScript(dscript, position+'的 script')
        energy = data.get('energy', missing)
        position += '的 energy '
        if energy != missing:
            dcapacity = energy.get('capacity', 1)
            isInt(dcapacity, position+'的 capacity')
            dtotalticks = energy.get('totalTicks', 1)
            isInt(dtotalticks, position+'的 totalTicks')
            dtype = energy.get('type', 'NONE')
            if dtype not in ('CAPACITOR', 'CONNECTOR', 'CONSUMER', 'GENERATOR', 'NONE'):
                report(position+'的 type')
                error('type 只能是 CAPACITOR、 CONNECTOR、 CONSUMER、 GENERATOR 或 NONE')
        items.add(i)

    lateinits = set()
    for scan_file in files['Machines']:
        printc(f'Loading machines: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)
        

def checkGenerators():
    global i, position
    
    def check(data):
        global i, position
        # necessary
        position = f'generators: {scan_file} 的 {i} '
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group')
        ditem = data['item']
        isItem(ditem, position+'的 item')
        isRecipe(data, position+'的 recipe')
        ioput = data['input'] + data['output']
        inSlots(i, ioput, position+'的 input 或 output')
        dcapacity = data['capacity']
        isInt(dcapacity, position+'的 capacity')
        dproduction = data['production']
        isInt(dproduction, position+'的 production')
        fuels = data['fuels']
        position += '的 fuels '
        for recipe in fuels.values():
            item = recipe['item']
            isItem(item, position+f'的 {recipe} 的 item')
            seconds = recipe['seconds']
            isInt(seconds, position+f'的 {recipe} 的 seconds')
            output = recipe['output']
            isItem(output, position+f'的 {recipe} 的 output')
        items.add(i)

    lateinits = set()
    for scan_file in files['Generators']:
        printc(f'Loading generators: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkSolarGenerators():
    global i, position
    
    def check(data):
        global i, position
        # necessary
        position = f'solar_generators: {scan_file} 的 {i} '
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group')
        ditem = data['item']
        isItem(ditem, position+'的 item')
        isRecipe(data, position+'的 recipe')
        dcapacity = data['capacity']
        isInt(dcapacity, position+'的 capacity')
        dday = data['dayEnergy']
        isInt(dday, position+'的 dayEnergy')
        dnight = data['nightEnergy']
        isInt(dnight, position+'的 nightEnergy')
        dlight = data['lightLevel']
        isInt(dlight, position+'的 lightLevel', 0, 15)
        items.add(i)

    lateinits = set()
    for scan_file in files['SolarGenerators']:
        printc(f'Loading solar_generators: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkMaterialGenerators():
    global i, position
    
    def check(data):
        global i, position
        # necessary
        position = f'mat_generators: {scan_file} 的 {i} '
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group')
        ditem = data['item']
        isItem(ditem, position+'的 item')
        isRecipe(data, position+'的 recipe')
        dcapacity = data['capacity']
        isInt(dcapacity, position+'的 capacity')
        outputItem = data['outputItem']
        isItem(outputItem, position+'的 outputItem')
        tickrate = data['tickRate']
        isInt(tickrate, position+'的 tickRate')
        status_slot = data['status']
        isInt(status_slot, position+'的 status', 0, 53)
        output = data['output']
        inSlots(i, output, position+'的 output', status_slot)
        per = data['per']
        isInt(per, position+'的 per')
        items.add(i)
    
    lateinits = set()
    for scan_file in files['MaterialGenerators']:
        printc(f'Loading mat_generators: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)
        

def checkRecipeMachines():
    global i, position

    def check(data):
        global i, position
        # necessary
        position = f'recipe_machines: {scan_file} 的 {i} '
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group')
        ditem = data['item']
        isItem(ditem, position+'的 item')
        isRecipe(data, position+'的 recipe')
        dinput = data['input']
        doutput = data['output']
        ioput = dinput + doutput
        inSlots(i, ioput, position+'的 input 或 output')
        dcapacity = data['capacity']
        isInt(dcapacity, position+'的 capacity')
        depc = data['energyPerCraft']
        isInt(depc, position+'的 energyPerCraft')
        speed = data['speed']
        isInt(speed, position+'的 speed')
        leninput = len(dinput)
        lenoutput = len(doutput)
        recipes = data['recipes']
        position += '的 recipes '
        for key, recipe in recipes.items():
            position = position + f'的 {key} '
            seconds = recipe['seconds']
            isInt(seconds, position+'的 seconds')
            chooseOne = recipe.get('chooseOne', False)
            isbool(chooseOne, 'chooseOne', position)
            temp = {}
            types = []
            recipe_input = recipe['input']
            if len(recipe_input) > leninput:
                report(position+'的 input')
                error('配方所需物品数量超过了输入槽位数')
            for o in recipe_input:
                ri = recipe_input[o]
                isItem(ri, position+f'的 input 的 {o}')
                itype = ri.get('material_type', 'mc')
                key = (ri['material'], itype)
                if key in temp:
                    temp[key] += 1
                else:
                    temp[key] = 1
                types.append(itype)
            for p in temp.values():
                if p > 1:
                    report(position+'的 input')
                    error('你不能设置输入超过两个相同物品！')
            for p in types:
                if types[0] == 'none':
                    report(position+'的 input')
                    error('你不能设置第一个物品的类型为none')
            temp = {}
            recipe_output = recipe['output']
            if len(recipe_output) > lenoutput:
                report(position+'的 output')
                error('配方输出物品数量超过了输出槽位数')
            for o in recipe_output:
                ro = recipe_output[o]
                isItem(ro, position+f'的 output 的 {o}')
                itype = ro.get('material_type', 'mc')
                key = (ro['material'], itype)
                if key in temp:
                    temp[key] += 1
                else:
                    temp[key] = 1
                types.append(itype)
            for p in temp.values():
                if p > 1:
                    report(position+'的 output')
                    error('你不能设置输入超过两个相同物品！')
            for p in types:
                if types[0] == 'none':
                    report(position+'的 output')
                    error('你不能设置第一个物品的类型为none')
        items.add(i)

    lateinits = set()
    for scan_file in files['RecipeMachines']:
        printc(f'Loading recipe_machines: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)
        
        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkSimpleMachines():
    global i, position
    
    def check(data):
        global i, position
        # necessary
        position = f'simple_machines: {scan_file} 的 {i} '
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group')
        ditem = data['item']
        isItem(ditem, position+'的 item')
        isRecipe(data, position+'的 recipe')
        settings = data['settings']
        dcapacity = settings['capacity']
        isInt(dcapacity, position+'的 settings 的 capacity')
        dconsumption = settings['consumption']
        isInt(dconsumption, position+'的 settings 的 consumption')
        dspeed = settings['speed']
        isInt(dspeed, position+'的 settings 的 speed')
        dtype = data['type']
        if dtype not in ('ELECTRIC_SMELTERY', 'ELECTRIC_FURNACE', 'ELECTRIC_GOLD_PAN', 'ELECTRIC_DUST_WASHER', 'ELECTRIC_ORE_GRINDER', 'ELECTRIC_INGOT_FACTORY', 'ELECTRIC_INGOT_PULVERIZER', 'CHARGING_BENCH'):
            report(position+'的 type')
            error('type 只能是 ELECTRIC_SMELTERY、 ELECTRIC_FURNACE、 ELECTRIC_GOLD_PAN、 ELECTRIC_DUST_WASHER、 ELECTRIC_ORE_GRINDER、 ELECTRIC_INGOT_FACTORY、 ELECTRIC_INGOT_PULVERIZER 或 CHARGING_BENCH')
        items.add(i)

    lateinits = set()
    for scan_file in files['SimpleMachines']:
        printc(f'Loading simple_machines: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkMultiblockMachines():
    global i, position
    
    def check(data):
        global i, position
        # necessary
        position = f'mb_machines: {scan_file} 的 {i} '
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group')
        ditem = data['item']
        isItem(ditem, position+'的 item')
        recipe = data['recipe']
        hasdispenser = False
        for key, avar in recipe.items():
            dtype = avar.get('material_type', 'mc')
            if dtype != 'mc':
                report(position+f'的 {key} 的 type')
                warn('方块只能是 mc 里的')
            material = avar['material']
            if material in ('DISPENSER', 'dispenser'):
                hasdispenser = True
        if not hasdispenser:
            report(position+'的 recipe')
            error('未找到发射器！')
        work = data['work']
        isInt(work, position+'的 work', 1, 9)
        sound = data['sound']
        isSound(sound, position+'的 sound')
        recipes = data['recipes']
        position += '的 recipes'
        for recipe in recipes.values():
            recipe_input = recipe['input']
            if len(recipe_input) > 9:
                report(position+'的 input')
                error('配方所需物品数量超过了输入槽位数')
            for o in recipe_input:
                ri = recipe_input[o]
                isItem(ri, position+f'的 input 的 {o}')
            recipe_output = recipe['output']
            isItem(recipe_output, position+'的 output')
        multiblock_types.add(i)
        items.add(i)

    lateinits = set()
    for scan_file in files['MultiblockMachines']:
        printc(f'Loading mb_machines: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkResearches():
    global i, position
    
    def check(data):
        global i, position
        # necessary
        position = f'researches: {scan_file} 的 {i} '
        loadReg(data, position)
        did = data['id']
        isInt(did, position+'的 id')
        for item in data['items']:
            isSlimefun(item, position+'的 items')

        # cannot have both
        dlc = data.get('levelCost', missing)
        dcc = data.get('currencyCost', missing)
        if dlc == missing:
            if dcc == missing:
                report(position)
                error('缺少 levelCost 或 currencyCost')
            else:
                isInt(dcc, position)
        else:
            isInt(dcc, position)

    lateinits = set()
    for scan_file in files['Researches']:
        printc(f'Loading researches: {scan_file}')
        with open(scan_file, 'r', encoding='utf-8') as f:
            k = getYamlContext(f)

        for i in k:
            data = k[i]
            if isLateInit(data):
                lateinits.add(i)
                continue
            check(data)

    for i in lateinits:
        data = k[i]
        check(data)


def checkAll():
    global i, position
    for checker in checkers:
        start = time()
        try:
            checker()
        except (yaml.scanner.ScannerError, yaml.parser.ParserError):
            error('在获取YAML内容时遇到了错误！')
            error('可能是YAML结构错误！请在下方网站内检查')
            error('https://www.bejson.com/validators/yaml_editor/')
        except KeyError:
            report(position)
            error('未找到参数！')
            error('可能是YAML缺少了参数或参数不完整！')
            error(f'相关信息 {i} {position}')
        print(f'{color.green}Spent {time() - start}s')
    print(f"{color.cyan}Done! {time() - sum_start}s")


try:
    sum_start = time()
    printc('Loading config')
    with open('RSCchecker-config.yml', 'r', encoding='utf-8') as file:
        config = getYamlContext(file)
    if config == {}:
        config = {'MaxPrintBug': MAXINT}
        error("读取config失败！你是否删除了RSCchecker-config.yml?")
    MaxBug = config['MaxPrintBug']
    MaxWarn = config['MaxPrintWarn']
    ignores = config['ignores']
    files = config['scan-files']
    checkers = [
        int if ignores['ignoreGroups'] else checkGroups,
        int if ignores['ignoreRecipeType'] else checkRecipeType,
        int if ignores['ignoreGeoResources'] else checkGeoResources,
        int if ignores['ignoreMobDrops'] else checkMobDrops,
        int if ignores['ignoreItems'] else checkItems,
        int if ignores['ignoreCapacitors'] else checkCapacitors,
        int if ignores['ignoreMenus'] else checkMenus,
        int if ignores['ignoreMachines'] else checkMachines,
        int if ignores['ignoreGenerators'] else checkGenerators,
        int if ignores['ignoreSolarGenerators'] else checkSolarGenerators,
        int if ignores['ignoreMaterialGenerators'] else checkMaterialGenerators,
        int if ignores['ignoreRecipeMachines'] else checkRecipeMachines,
        int if ignores['ignoreSimpleMachines'] else checkSimpleMachines,
        int if ignores['ignoreMultiblockMachines'] else checkMultiblockMachines,
        int if ignores['ignoreResearches'] else checkResearches,
        int if ignores['ignorePerhapedRecipeType'] else checkPerhapedRecipeType
    ]
    RewriteSlimefunItems()
    SlimefunItems = set(getSlimefunItems())
    loadedItems = getVanillaItems()
    VanillaItems = set((tuple(i.keys())[0] for i in loadedItems))
    scripts = getScripts()
    keys = []
    values = []
    for item in loadedItems:
        keys.append(tuple(item.keys())[0])
        values.append(tuple(item.values())[0])
    MaxStacks = dict(zip(keys, values))
    saveditems = getSaveditems()
    entities = set()
    for item in VanillaItems:
        if item[-10:] == '_SPAWN_EGG':
            entities.add(item[:-10])
    entities.add("GIANT")
    checkAll()
    print(f'{color.cyan}共{totalBug}个Bug')
    print(f'{color.cyan}共{totalWarn}个Warn')
    print(f'{color.cyan}此脚本实际上并不能找到全部的Bug')
    print(f'{color.cyan}只能尽可能找出潜在的Bug！')
except FileNotFoundError as err:
    error('无法找到文件！')
    error(err)
except BaseException:  # 任何错误
    error('运行程序时遇到了致命错误，请查看错误信息，确定并非自己的问题后，可联系作者修复！')
    error(f'在检查 {i} 时遇到了错误，可能是缺少必需参数！')
    error(f'相关信息 {position}')

"""
'请确保控制台输出的bug（若有）皆已修复，本程序才能正常运行！'
'需要注意的是，此脚本并不会检查任何与name或lore相关的内容！'
'如有误报请联系作者企鹅2793572961'
'此python程序任何人皆可使用，修改，但不得进行任何商业活动、违反公德的行为或违法行为'
'Made by guguguhello'
"""

