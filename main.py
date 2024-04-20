# coding=utf-8

import os
import yaml

from time import time

_VERSION = '1.3 REALEASE'
MAXINT = 2147483647
recipe_types = set("ENHANCED_CRAFTING_TABLE, MAGIC_WORKBENCH, ARMOR_FORGE, COMPRESSOR, PRESSURE_CHAMBER, SMELTERY, ORE_CRUSHER, GRIND_STONE, ANCIENT_ALTAR, NULL, GEO_MINER".split(', '))
BIOMES = set("BADLANDS  BAMBOO_JUNGLE  BASALT_DELTAS  BEACH  BIRCH_FOREST  CHERRY_GROVE  COLD_OCEAN  CRIMSON_FOREST  CUSTOM DARK_FOREST  DEEP_COLD_OCEAN  DEEP_DARK  DEEP_FROZEN_OCEAN  DEEP_LUKEWARM_OCEAN  DEEP_OCEAN  DESERT  DRIPSTONE_CAVES  END_BARRENS  END_HIGHLANDS  END_MIDLANDS  ERODED_BADLANDS  FLOWER_FOREST  FOREST  FROZEN_OCEAN  FROZEN_PEAKS  FROZEN_RIVER  GROVE  ICE_SPIKES  JAGGED_PEAKS  JUNGLE  LUKEWARM_OCEAN  LUSH_CAVES  MANGROVE_SWAMP  MEADOW  MUSHROOM_FIELDS  NETHER_WASTES  OCEAN  OLD_GROWTH_BIRCH_FOREST  OLD_GROWTH_PINE_TAIGA  OLD_GROWTH_SPRUCE_TAIGA  PLAINS  RIVER  SAVANNA  SAVANNA_PLATEAU  SMALL_END_ISLANDS  SNOWY_BEACH  SNOWY_PLAINS  SNOWY_SLOPES  SNOWY_TAIGA  SOUL_SAND_VALLEY  SPARSE_JUNGLE  STONY_PEAKS  STONY_SHORE  SUNFLOWER_PLAINS  SWAMP  TAIGA  THE_END  THE_VOID  WARM_OCEAN  WARPED_FOREST  WINDSWEPT_FOREST  WINDSWEPT_GRAVELLY_HILLS  WINDSWEPT_HILLS  WINDSWEPT_SAVANNA  WOODED_BADLANDS  OTHERS".split('  '))
sounds = set('ANCIENT_ALTAR_FINISH_SOUND ANCIENT_ALTAR_ITEM_CHECK_SOUND ANCIENT_ALTAR_ITEM_DROP_SOUND ANCIENT_ALTAR_ITEM_PICK_UP_SOUND ANCIENT_ALTAR_START_SOUND ANCIENT_PEDESTAL_ITEM_PLACE_SOUND ARMOR_FORGE_FINISH_SOUND ARMOR_FORGE_WORKING_SOUND AUTO_CRAFTER_GUI_CLICK_SOUND AUTO_CRAFTER_UPDATE_RECIPE AUTOMATED_PANNING_MACHINE_FAIL_SOUND AUTOMATED_PANNING_MACHINE_SUCCESS_SOUND BACKPACK_CLOSE_SOUND BACKPACK_OPEN_SOUND BEE_BOOTS_FALL_SOUND COMPOSTER_COMPOST_SOUND COMPRESSOR_CRAFT_CONTRACT_SOUND COMPRESSOR_CRAFT_EXTEND_SOUND COMPRESSOR_CRAFT_SOUND COOLER_CONSUME_SOUND CRUCIBLE_ADD_LAVA_SOUND CRUCIBLE_ADD_WATER_SOUND CRUCIBLE_BLOCK_BREAK_SOUND CRUCIBLE_GENERATE_LIQUID_SOUND CRUCIBLE_INTERACT_SOUND CRUCIBLE_PLACE_LAVA_SOUND CRUCIBLE_PLACE_WATER_SOUND DEBUG_FISH_CLICK_SOUND DIET_COOKIE_CONSUME_SOUND ELYTRA_CAP_IMPACT_SOUND ENCHANTMENT_RUNE_ADD_ENCHANT_SOUND ENDER_BACKPACK_OPEN_SOUND ENHANCED_CRAFTING_TABLE_CRAFT_SOUND EXPLOSIVE_BOW_HIT_SOUND EXPLOSIVE_TOOL_EXPLODE_SOUND FISHERMAN_ANDROID_FISHING_SOUND FLASK_OF_KNOWLEDGE_FILLUP_SOUND GPS_NETWORK_ADD_WAYPOINT GPS_NETWORK_CREATE_WAYPOINT GPS_NETWORK_OPEN_PANEL_SOUND GRIND_STONE_INTERACT_SOUND GUIDE_BUTTON_CLICK_SOUND GUIDE_CONTRIBUTORS_OPEN_SOUND GUIDE_LANGUAGE_OPEN_SOUND GUIDE_OPEN_SETTING_SOUND IGNITION_CHAMBER_USE_FLINT_AND_STEEL_SOUND INFUSED_HOPPER_TELEPORT_SOUND INFUSED_MAGNET_TELEPORT_SOUND IRON_GOLEM_ASSEMBLER_ASSEMBLE_SOUND JETBOOTS_THRUST_SOUND JETPACK_THRUST_SOUND JUICER_USE_SOUND LIMITED_USE_ITEM_BREAK_SOUND MAGIC_SUGAR_CONSUME_SOUND MAGIC_WORKBENCH_FINISH_SOUND MAGIC_WORKBENCH_START_ANIMATION_SOUND MAGICAL_EYE_OF_ENDER_USE_SOUND MINER_ANDROID_BLOCK_GENERATION_SOUND MINING_TASK_SOUND ORE_WASHER_WASH_SOUND PLAYER_RESEARCHING_SOUND PORTABLE_CRAFTER_OPEN_SOUND PORTABLE_DUSTBIN_OPEN_SOUND PRESSURE_CHAMBER_FINISH_SOUND PRESSURE_CHAMBER_WORKING_SOUND PROGRAMMABLE_ANDROID_SCRIPT_DOWNLOAD_SOUND SLIME_BOOTS_FALL_SOUND SMELTERY_CRAFT_SOUND SOULBOUND_RUNE_RITUAL_SOUND SPLINT_CONSUME_SOUND STOMPER_BOOTS_STOMP_SOUND TAPE_MEASURE_MEASURE_SOUND TELEPORT_SOUND TELEPORT_UPDATE_SOUND TELEPORTATION_MANAGER_OPEN_GUI TOME_OF_KNOWLEDGE_USE_SOUND VAMPIRE_BLADE_HEALING_SOUND VANILLA_AUTO_CRAFTER_UPDATE_RECIPE_SOUND VILLAGER_RUNE_TRANSFORM_SOUND VITAMINS_CONSUME_SOUND WIND_STAFF_USE_SOUND'.split(' '))
RainbowTypes = set('GLASS_PANE, GLASS, STAINED_GLASS, STAINED_GLASS_PANE, WOOL, TERRACOTTA, CUSTOM, GLAZED_TERRACOTTA, TERRACOTTA_ALL'.split(', '))
simpleMachinesTypes = set(('ELECTRIC_SMELTERY', 'ELECTRIC_FURNACE', 'ELECTRIC_GOLD_PAN', 'ELECTRIC_DUST_WASHER', 'ELECTRIC_ORE_GRINDER', 'ELECTRIC_INGOT_FACTORY', 'ELECTRIC_INGOT_PULVERIZER', 'CHARGING_BENCH', 'TREE_GROWTH_ACCELERATOR', 'ANIMAL_GROWTH_ACCELERATOR', 'CROP_GROWTH_ACCELERATOR'))
protection_types = ['BEES', 'RADIATION', 'FLYING_INTO_WALL']
armor_levels = ['LEATHER', 'CHAINMAIL', 'IRON', 'DIAMOND', 'GOLDEN', 'NETHERITE']
effects = {'SPEED', 'SLOWNESS', 'HASTE', 'MINING_FATIGUE', 'STRENGTH', 'INSTANT_HEALTH', 'INSTANT_DAMAGE', 'JUMP_BOOST', 'NAUSEA', 'REGENERATION', 'RESISTANCE', 'FIRE_RESISTANCE', 'WATER_BREATHING', 'INVISIBILITY', 'BLINDNESS', 'NIGHT_VISION', 'HUNGER', 'WEAKNESS', 'POISON', 'WITHER', 'HEALTH_BOOST', 'ABSORPTION', 'SATURATION', 'GLOWING', 'LEVITATION', 'LUCK', 'UNLUCK', 'SLOW_FALLING', 'CONDUIT_POWER', 'DOLPHINS_GRACE', 'BAD_OMEN', 'HERO_OF_THE_VILLAGE', 'DARKNESS'}
bhelmets = [level+'_HELMET' for level in armor_levels]
bchestplates = [level+'_CHESTPLATE' for level in armor_levels]
bleggings = [level+'_LEGGINGS' for level in armor_levels]
bboots = [level+'_BOOTS' for level in armor_levels]

bhelmets.append('TURTLE_HELMET')
bchestplates.append('ELYTRA')
null = '__MISSING_STRING_RSCCHECKER'
radiation_levels = {'HIGH', 'LOW', 'MODERATE', 'VERY_HIGH', 'VERY_DEADLY', null}

saveditems = set()
parentsGroups = set()
normalGroups = set()
items = set()
default_recipe = [{'material_type': 'none'}]*9
machines_slots = {}
lateinit_recipe_type = {}
totalBug = 0
totalWarn = 0
i = 'loading config'
position = 'loading config'
r = range(1, 10)


class color:
    # Text color
    black = '\33[30m'
    red = '\33[31m'
    green = '\33[32m'
    gold = '\33[33m'
    blue = '\33[34m'
    purple = '\33[35m'
    cyan = '\33[36m'
    lightgray = lightgrey = '\33[37m'
    gray = grey = '\33[38m'
    white = reset = '\33[39m'

    # Background color
    bblack = '\33[40m'
    bred = '\33[41m'
    bgreen = '\33[42m'
    bgold = '\33[43m'
    bblue = '\33[44m'
    bpurple = '\33[45m'
    bcyan = '\33[46m'
    blightgray = blightgrey = '\33[47m'
    bgray = bgrey = '\33[48m'
    bwhite = '\33[49m'


def error(string, end='\n'):
    if totalBug < config['MaxPrintBug']:
        print(f'{color.red}{string}{color.reset}', end=end)


def warn(string, end='\n'):
    print(f'{color.gold}{string}{color.reset}', end=end)


def report(position, Warn=False):
    global config, totalBug, totalWarn, MaxBug, MaxWarn
    if Warn and totalWarn == MaxWarn:
        totalWarn += 1
        error(f"[Warn]{totalWarn}. 在 {position}:", end="\n  ")
        error("[Warn] Warn打印数量已达到上限！")
    elif Warn and totalWarn < MaxWarn:
        totalWarn += 1
        warn(f"[WARN]{totalWarn}. 在 {position}:", end="\n  ")
    elif totalBug == MaxBug:
        totalBug += 1
        error(f"[BUG]{totalBug}. 在 {position}:", end="\n  ")
        error("[BUG] Bug数量已达到上限！请修复以上Bug再运行本程序！")
    elif totalBug < MaxBug:
        totalBug += 1
        error(f"[BUG]{totalBug}. 在 {position}:", end="\n  ")


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
        file_path = os.path.join(current_directory, "..\\Slimefun\\Items.yml")
    else:
        file_path = config['SlimefunItemsPath']
    with open(file_path, 'r', encoding='utf-8') as file:
        regNames = getYamlContext(file).keys()
    with open('__SlimefunItems.yml', 'w', encoding='utf-8') as file:
        yaml.dump({'items': list(regNames)}, file, allow_unicode=True, encoding='utf-8')


def getSaveditems(addon):
    items = set()
    for root, dirs, files in os.walk(f"addons/{addon}/saveditems"):
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


def inSlimefun(item): return item in SlimefunItems
def inVanilla(item): return item.upper() in VanillaItems
def inSaveditems(item): return item in saveditems
def inBiome(item): return item.upper() in BIOMES
def inScripts(item): return str(item) in scripts
def inSound(item): return item.upper() in sounds
def inRainbowTypes(dtype): return dtype in RainbowTypes
def inHelmets(item): return item.upper() in bhelmets
def inChestplates(item): return item.upper() in bchestplates
def inLeggings(item): return item.upper() in bleggings
def inBoots(item): return item.upper() in bboots


def isVanilla(item, position):
    if not inVanilla(item):
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
    if item == null:
        return
    if not inScripts(str(item)):
        report(position)
        error(f"{item} 可能不是正确的脚本名称")


def isRainbowType(dtype, position):
    if not inRainbowTypes(dtype):
        report(position+'的 rainbow')
        error(f'{dtype} 不是有效的类型')


def isHelmet(item, position):
    if not inHelmets(item):
        report(position)
        error(f'{item} 不是有效的头盔！')


def isChestplate(item, position):
    if not inChestplates(item):
        report(position)
        error(f'{item} 不是有效的胸甲！')


def isLeggings(item, position):
    if not inLeggings(item):
        report(position)
        error(f'{item} 不是有效的护腿！')


def isBoots(item, position):
    if not inBoots(item):
        report(position)
        error(f'{item} 不是有效的靴子！')


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
    return MaxStacks[item.upper()]


def isAmountProper(item, dAm, position, zero=False, warn=False):
    stack = getItemMaxStack(item) if inVanilla(str(item)) else 64
    isInt(dAm, f'{position}', 0 if (stack == 0 or zero) else 1, stack, warn)


def isbool(dat, arg, position):
    if not (dat is True or dat is False):
        report(f'{position} 的 {arg}')
        error(f'{arg} 只能是 true 或 false')


def isItem(data, position, Warn=False):
    # necessary
    dtype = data.get('material_type', 'mc')
    did = data.get('material', null)
    if dtype == 'mc':
        isVanilla(did, position+'的 material_type')
    elif dtype == 'slimefun':
        isSlimefun(did, position+'的 material_type')
    elif dtype == 'saveditem':
        isSaveditem(did, position+'的 material_type')
    elif did == null and dtype != 'none':
        report(position)
        error('缺少参数 material')
    elif dtype not in ('none', 'skull_base64', 'skull_url', 'skull_hash'):
        report(position+'的 material_type')
        error('type 只能是 mc、 slimefun、 saveditem、 none、 skull_base64、 skull_url 或 skull_hash！')
    if dtype != 'none':
        dam = data.get('amount', 1)
        isAmountProper(did, dam, position+'的 amount', warn=Warn)

    # not necessary
    dmodelid = data.get('modelId', 0)
    isInt(dmodelid, position)


def isRecipe(data, position):
    recipe_type = data.get('recipe_type', null)
    recipe = default_recipe
    load_recipe = data.get('recipe', {})
    for bvar in load_recipe:
        if bvar in r:
            isItem(load_recipe[bvar], f'{position} 的 {bvar} ')
            item = load_recipe.get('material', null)
            recipe[bvar-1] = {
                'material': item,
                'material_type': load_recipe.get('material_type', 'mc' if item != null else 'none'),
                'amount': load_recipe.get('amount', 1)
            }
        else:
            report(position, True)
            warn(f"{bvar}是无效的编号，有效编号是1-9的数字，此编号会被无视")
    if recipe_type == null:
        if recipe != default_recipe:
            report(position)
            error('缺少 recipe_type')
        else:
            recipe_type = 'null'
    else:
        isRecipeType(recipe_type, position)
    idx = 1
    if recipe_type in {'ENHANCED_CRAFTING_TABLE', 'MAGIC_WORKBENCH', 'ARMOR_FORGE', 'PRESSURE_CHAMBER'}:
        for k in recipe:
            if k['material_type'] != 'none' and k['amount'] != 1:
                report(position+f'的 crafting-recipe 的 第 {idx} 个物品')
                error('amount 必须为 1')
            idx += 1
    elif recipe_type in {'COMPRESSOR', 'PRESSURE_CHAMBER', 'ORE_CRUSHER', 'GRIND_STONE'}:
        for k in recipe[1:]:
            if k['material_type'] != 'none' and k['material'] != null:
                report(position+f'的 crafting-recipe 的 第 {idx} 个物品')
                error(f"第{idx}槽必须为 none 类型")
            idx += 1 
    elif recipe_type == "ANCIENT_ALTAR":
        for k in recipe:
            if k['material_type'] == 'none' and k['material'] != null:
                report(position+f'的 crafting-recipe 的 第 {idx} 个物品的 type')
                error(f"第{idx}槽必须不为 none 类型")
            if k['material_type'] != 'none' and k['amount'] != 1:
                report(position+f'的 crafting-recipe 的 第 {idx} 个物品的 type')
                error(f"第{idx}槽的 amount 必须为 1")
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
    dlateinit = isLateInit(data)
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
        error(f'{group} 可能不是个有效的分类，如果是非自定义分类请无视此警告')


def isRecipeType(recipe_type, position):
    if recipe_type not in recipe_types:
        lateinit_recipe_type[position] = recipe_type


def inSlots(name, slots, position, status_slot=-1):
    ms = machines_slots.get(name, null)
    if ms == null:
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
        elif isinstance(j, str):
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
                error(f'{rang} 可能不是有效的 slot ')
        else:
            report(position)
            error(f'{j} 只能是整数或字符串！')
    return fs


def checkPotionEffects(data):
    global i, position
    potion_effects = data.get('potion_effects', [])
    for string in potion_effects:
        position = f"{position}的 potion_effects 的 '{string}'"
        split = string.split(' ')
        if len(split) != 2:
            report(position)
            error('参数格式错误！应为 - "SPEED 5" ')
            continue
        effect = split[0]
        amp = int(split[1])
        if effect not in effects:
            report(position)
            error(f'{effect} 不是有效的状态效果')
        if amp < 0:
            report(position)
            error(f'药水效果等级必须是非负整数，但读取到了{amp}')


def checkGroups(addon):
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
            parent = data.get('parent', null)
            if parent == null:
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
        dtier = data.get('tier', 1)
        isInt(dtier, position+'的 tier', 1)
        dhidden = data.get('hidden', False)
        isbool(dhidden, 'hidden', position+'的 hidden')

    lateinits = set()
    scan_file = "addons/"+addon+"/groups.yml"
    printc(f'Loading groups: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkRecipeTypes(addon):
    global i, position
    
    def check(data):
        global i, position
        position = f'recipe_types: {scan_file} 的 {i} '
        loadReg(data, position)
        isItem(data, position+'的 item')
        recipe_types.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/recipe_types.yml"
    printc(f'Loading recipe_types: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkGeoResources(addon):
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
    scan_file = "addons/"+addon+"/geo_resources.yml"
    printc(f'Loading geo_resources: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkMobDrops(addon):
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
    scan_file = "addons/"+addon+"/mob_drops.yml"
    printc(f'Loading mob_drops: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)

    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkItems(addon):
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
        dscript = data.get('script', null)
        isScript(dscript, position+'的 script')
        dglow = data.get('glow', False)
        isbool(dglow, 'glow', position)
        drainbow = data.get('rainbow', 'WOOL')
        isRainbowType(drainbow, position+'的 rainbow 的 {ritem}')
        if drainbow == 'CUSTOM':
            rainbow_materials = data.get('rainbow_materials', null)
            if rainbow_materials == null:
                report(position)
                error('缺少 rainbow_materials')
            for ritem in rainbow_materials:
                isVanilla(ritem, position+'的 rainbow_materials')
        danti_wither = data.get('anti_wither', False)
        isbool(danti_wither, 'anti_wither', position)
        dsoulbound = data.get('soulbound', False)
        isbool(dsoulbound, 'soulbound', position)
        dvanilla = data.get('vanilla', False)
        isbool(dvanilla, 'vanilla', position)
        energy_capacity = data.get('energy_capacity', 0)
        isInt(energy_capacity, position+'的 energy_capacity')
        radiation = data.get('radiation', null)
        if radiation not in radiation_levels:
            report(position+'的 radiation')
            error(f'{radiation} 不是正确的辐射等级')
        piglin_trade = data.get('piglin_trade', {})
        piglin_trade_chance = piglin_trade.get('piglin_trade_chance', 0)
        isInt(piglin_trade_chance, position+'的 piglin_trade 的 piglin_trade_chance')

        items.add(i)
    
    lateinits = set()
    scan_file = "addons/"+addon+"/items.yml"
    printc(f'Loading items: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkArmors(addon):
    global i, position

    def check(data):
        global i, position
        position = f'armors: {scan_file} 的 {i}'
        loadReg(data, position)
        fullset = data.get('fullSet', False)
        isbool(fullset, 'fullSet', position)
        item_group = data['item_group']
        isGroup(item_group, position+'的 item_group')
        dpts = data['protection_types']
        for dpt in dpts:
            if dpt not in protection_types:
                report(position+'的 protection_types')
                error(f'{dpt} 不是有效的盔甲保护类型')
        
        helmet = data.get('helmet', null)
        chestplate = data.get('chestplate', null)
        leggings = data.get('leggings', null)
        boots = data.get('boots', null)
        if null == helmet == chestplate == leggings == boots:
            report(position)
            error('没有设置任何装备！')
        if helmet != null:
            isRecipe(helmet, position)
            isHelmet(helmet['material'], position+'的 material')
            checkPotionEffects(helmet)
            items.add(helmet['id'])
        if chestplate != null:
            isRecipe(chestplate, position)
            isChestplate(chestplate['material'], position+'的 material')
            checkPotionEffects(chestplate)
            items.add(chestplate['id'])
        if leggings != null:
            isRecipe(leggings, position)
            isLeggings(leggings['material'], position+'的 material')
            checkPotionEffects(leggings)
            items.add(leggings['id'])
        if boots != null:
            isRecipe(boots, position)
            isBoots(boots['material'], position+'的 material')
            checkPotionEffects(boots)
            items.add(boots['id'])

    lateinits = set()
    scan_file = "addons/"+addon+"/armors.yml"
    printc(f'Loading armors: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkCapacitors(addon):
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
        isInt(dcapacity, position+'的 capacity', 1)
        isRecipe(data, position+'的 recipe')
        items.add(i)
        
    lateinits = set()
    scan_file = "addons/"+addon+"/capacitors.yml"
    printc(f'Loading capacitors: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkMenus(addon):
    global i, position
    
    def check(data):
        global i, position
        position = f'menus: {scan_file} 的 {i} '
        loadReg(data, position)
        dimport = data.get('import', null)
        if dimport == null:
            dtitle = data.get('title', null)
            if dtitle == null:
                report(position+'的 title')
                error("缺少 title！")
            slots = data['slots']
            for slot in slots:
                s = slots[slot]
                isItem(s, position+f'的 {slot}')
                progressbar = s.get('progressbar', False)
                isbool(progressbar, 'progressbar', position)
            machines_slots[i] = slot_read(slots, position+'的 slots')
        else:
            if dimport not in machines_slots:
                report(position+'的 import')
                error(f'{dimport} 可能不是有效的机器菜单')

    lateinits = set()
    scan_file = "addons/"+addon+"/menus.yml"
    printc(f'Loading menus: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkMachines(addon):
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
        dscript = data.get('script', null)
        isScript(dscript, position+'的 script')
        energy = data.get('energy', null)
        position += '的 energy '
        if energy != null:
            dcapacity = energy.get('capacity', 0)
            isInt(dcapacity, position+'的 capacity')
            dtotalticks = energy['totalTicks']
            isInt(dtotalticks, position+'的 totalTicks', 1)
            dtype = energy.get('type', 'NONE')
            if dtype not in ('CAPACITOR', 'CONNECTOR', 'CONSUMER', 'GENERATOR', 'NONE'):
                report(position+'的 type')
                error('type 只能是 CAPACITOR、 CONNECTOR、 CONSUMER、 GENERATOR 或 NONE')
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/machines.yml"
    printc(f'Loading machines: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkGenerators(addon):
    global i, position

    def check(data):
        global i, position
        # necessary
        position = f'generators: {scan_file} 的 {i} '
        loadReg(data, position)
        dgroup = data['item_group']
        isGroup(dgroup, position+'的 item_group ')
        ditem = data['item']
        isItem(ditem, position+'的 item ')
        isRecipe(data, position+'的 recipe ')
        ioput = data['input'] + data['output']
        inSlots(i, ioput, position+'的 input 或 output ')
        dcapacity = data.get('capacity', 0)
        isInt(dcapacity, position+'的 capacity')
        dproduction = data['production']
        isInt(dproduction, position+'的 production', 1)
        fuels = data['fuels']
        position += '的 fuels '
        for ddk in fuels:
            recipe = fuels[ddk]
            item = recipe['item']
            isItem(item, position+f'的 {ddk} 的 item')
            seconds = recipe['seconds']
            isInt(seconds, position+f'的 {ddk} 的 seconds')
            output = recipe['output']
            isItem(output, position+f'的 {ddk} 的 output ')
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/generators.yml"
    printc(f'Loading generators: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkSolarGenerators(addon):
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
        isInt(dcapacity, position+'的 capacity', 1)
        dday = data['dayEnergy']
        isInt(dday, position+'的 dayEnergy', 1)
        dnight = data['nightEnergy']
        isInt(dnight, position+'的 nightEnergy', 1)
        dlight = data['lightLevel']
        isInt(dlight, position+'的 lightLevel', 0, 15)
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/solar_generators.yml"
    printc(f'Loading solar_generators: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkMaterialGenerators(addon):
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
        isInt(dcapacity, position+'的 capacity', 1)
        outputItem = data['outputItem']
        isItem(outputItem, position+'的 outputItem ', Warn=True)
        tickrate = data['tickRate']
        isInt(tickrate, position+'的 tickRate', 1)
        status_slot = data['status']
        isInt(status_slot, position+'的 status', 0, 53)
        output = data['output']
        inSlots(i, output, position+'的 output', status_slot)
        per = data['per']
        isInt(per, position+'的 per', 1)
        items.add(i)
    
    lateinits = set()
    scan_file = "addons/"+addon+"/mat_generators.yml"
    printc(f'Loading mat_generators: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkRecipeMachines(addon):
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
        isInt(dcapacity, position+'的 capacity', 0)
        depc = data['energyPerCraft']
        isInt(depc, position+'的 energyPerCraft', 1)
        if dcapacity < depc:
            report(position)
            error('合成一次的消耗能量不能大于能量容量！')
        speed = data.get('speed', 1)
        isInt(speed, position+'的 speed', 1)
        leninput = len(dinput)
        lenoutput = len(doutput)
        recipes = data['recipes']
        position += '的 recipes '
        BP = position
        for key, recipe in recipes.items():
            position = BP + f'的 {key} '
            seconds = recipe['seconds']
            isInt(seconds, position+'的 seconds', 1)
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
                itype = ri.get('material_type', 'mc')
                isItem(ri, position+f'的 input 的 {o}')
                key = (ri['material'], itype)
                if key in temp:
                    temp[key] += 1
                else:
                    temp[key] = 1
                types.append(itype)
            for p in temp.values():
                if p > 1:
                    report(position+'的 input')
                    error('你不能设置输入两个或以上相同物品！')
                    error('According to Slimefun Github Issue #4166. ')
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
                itype = ro.get('material_type', 'mc')
                isItem(ro, position+f'的 output 的 {o}')
                key = (ro['material'], itype)
                if key in temp:
                    temp[key] += 1
                else:
                    temp[key] = 1
                types.append(itype)
            for p in types:
                if types[0] == 'none':
                    report(position+'的 output')
                    error('你不能设置第一个物品的类型为none')
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/recipe_machines.yml"
    printc(f'Loading recipe_machines: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkSimpleMachines(addon):
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
        isInt(dcapacity, position+'的 settings 的 capacity', 1)
        dconsumption = settings['consumption']
        isInt(dconsumption, position+'的 settings 的 consumption', 1)
        dspeed = settings.get('speed', 1)
        isInt(dspeed, position+'的 settings 的 speed', 1)
        dradius = settings.get('radius', 1)
        isInt(dradius, position+'的 settings 的 radius', 1)
        dtype = data['type']
        if dtype not in simpleMachinesTypes:
            report(position+'的 type')
            error(f'{type} 不是有效的 type')
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/simple_machines.yml"
    printc(f'Loading simple_machines: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkMultiblockMachines(addon):
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
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/mb_machines.yml"
    printc(f'Loading mb_machines: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkResearches(addon):
    global i, position

    def check(data):
        global i, position
        # necessary
        position = f'researches: {scan_file} 的 {i} '
        loadReg(data, position)
        did = data['id']
        isInt(did, position+'的 id')
        name = data.get('name', null)
        if name == null:
            report(position+'的 name')
            error('不能缺少名字！')
        else:
            for s in name:
                if s in 'abcdefghijklmnopqrstuvwxyz0123456789.-_':
                    report(position)
                    error('研究ID只能由 abcdefghijklmnopqrstuvwxyz0123456789.-_ 中的字符组成')
                    break

        for item in data['items']:
            isSlimefun(item, position+'的 items')

        # special
        dlc = data.get('levelCost', null)
        dcc = data.get('currencyCost', null)
        flag = True
        if dlc != null:
            isInt(dlc, position+'的 levelCost', 1)
            flag = False
        if dcc != null:
            isInt(dcc, position+'的 currencyCost', 1)
            flag = False
        if flag:
            report(position)
            error("缺少 levelCost 或 currencyCost")

    lateinits = set()
    scan_file = "addons/"+addon+"/researches.yml"
    printc(f'Loading researches: {scan_file}')
    with open(scan_file, 'r', encoding='utf-8') as f:
        k = getYamlContext(f)

    for i in k:
        data = k[i]
        if isLateInit(data):
            lateinits.add(i)
            continue
        check(data)
    yield
    for i in lateinits:
        data = k[i]
        check(data)
    yield


def checkAll():
    global i, position, saveditems
    chs = []
    for addon in addons:
        saveditems = getSaveditems(addon)
        for checker in checkers:
            chs.append(checker(addon))
        try:
            for __ in range(2):
                if __ == 1:
                    print(f'{color.gold} loading lateInit items:')
                for ch in chs:
                    start = time()
                    next(ch)
                    print(f'{color.green}Spent {time() - start}s')
        except (yaml.scanner.ScannerError, yaml.parser.ParserError):
            error('在获取YAML内容时遇到了错误！')
            error('可能是YAML结构错误！请在下方网站内检查')
            error('https://www.bejson.com/validators/yaml_editor/')
        except KeyError:
            report(position)
            error('未找到参数！')
            error('可能是YAML缺少了参数或参数不完整！')
            error(f'相关信息 {i} {position}')

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
    scan_files = config['scan-files']
    addons = scan_files['addons']
    checkers = [
        # int just a placeholder
        int if ignores['ignoreGroups'] else checkGroups,
        int if ignores['ignoreRecipeTypes'] else checkRecipeTypes,
        int if ignores['ignoreGeoResources'] else checkGeoResources,
        int if ignores['ignoreMobDrops'] else checkMobDrops,
        int if ignores['ignoreItems'] else checkItems,
        int if ignores['ignoreArmors'] else checkArmors,
        int if ignores['ignoreCapacitors'] else checkCapacitors,
        int if ignores['ignoreMenus'] else checkMenus,
        int if ignores['ignoreGenerators'] else checkGenerators,
        int if ignores['ignoreSolarGenerators'] else checkSolarGenerators,
        int if ignores['ignoreMaterialGenerators'] else checkMaterialGenerators,
        int if ignores['ignoreMachines'] else checkMachines,
        int if ignores['ignoreRecipeMachines'] else checkRecipeMachines,
        int if ignores['ignoreSimpleMachines'] else checkSimpleMachines,
        int if ignores['ignoreMultiblockMachines'] else checkMultiblockMachines,
        int if ignores['ignoreResearches'] else checkResearches
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
finally:...
"""
'请确保控制台输出的bug（若有）皆已修复，本程序才能正常运行！'
'需要注意的是，此脚本并不会检查任何与name或lore相关的内容！'
'如有误报请联系作者企鹅2793572961'
'此python程序任何人皆可使用，修改，但不得进行任何商业活动、违反公德的行为或违法行为'
'Made by guguguhello'
"""

