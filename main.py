# coding=utf-8
# flake8: noqa: E501
# flake8: noqa: E902
# pylint: disable=line-too-long,too-many-lines,missing-module-docstring,invalid-name,missing-function-docstring,redefined-outer-name,wrong-import-order,global-variable-not-assigned,trailing-whitespace,used-before-assignment,f-string-without-interpolation,global-statement,multiple-statements,import-error,unused-variable,unused-argument,undefined-loop-variable,anomalous-backslash-in-string,global-variable-undefined,too-many-statements,too-many-branches,too-many-locals,missing-class-docstring,too-few-public-methods

import os
import yaml

from datetime import datetime
from time import time
from typing import Generator, Any

_VERSION = "1.6 SNAPSHOT"


class color:
    # Text color
    black = "\33[30m"
    red = "\33[31m"
    green = "\33[32m"
    gold = "\33[33m"
    blue = "\33[34m"
    purple = "\33[35m"
    cyan = "\33[36m"
    lightgray = lightgrey = "\33[37m"
    gray = grey = "\33[38m"
    white = reset = "\33[39m"

    # Background color
    bblack = "\33[40m"
    bred = "\33[41m"
    bgreen = "\33[42m"
    bgold = "\33[43m"
    bblue = "\33[44m"
    bpurple = "\33[45m"
    bcyan = "\33[46m"
    blightgray = blightgrey = "\33[47m"
    bgray = bgrey = "\33[48m"
    bwhite = "\33[49m"

REPORT_BUGS = f"{color.cyan}Report bugs here {color.green}https://github.com/SlimefunReloadingProject/RSCchecker/issues in English or Chinese"
BIG_THANKS = f"{color.cyan}Big thanks to {color.green}https://github.com/SlimefunReloadingProject"
MAXINT = 2147483647
RECIPE_TYPES = set("ENHANCED_CRAFTING_TABLE, MAGIC_WORKBENCH, ARMOR_FORGE, COMPRESSOR, PRESSURE_CHAMBER, SMELTERY, ORE_CRUSHER, GRIND_STONE, ANCIENT_ALTAR, NULL, MULTIBLOCK, GEO_MINER, GOLD_PAN, JUICER, MOB_DROP, BARTER_DROP, INTERACT, HEATED_PRESSURE_CHAMBER, FOOD_FABRICATOR, FOOD_COMPOSTER, FREEZER, REFINERY, NUCLEAR_REACTOR".split(", "))
BIOMES = set("BADLANDS  BAMBOO_JUNGLE  BASALT_DELTAS  BEACH  BIRCH_FOREST  CHERRY_GROVE  COLD_OCEAN  CRIMSON_FOREST  CUSTOM DARK_FOREST  DEEP_COLD_OCEAN  DEEP_DARK  DEEP_FROZEN_OCEAN  DEEP_LUKEWARM_OCEAN  DEEP_OCEAN  DESERT  DRIPSTONE_CAVES  END_BARRENS  END_HIGHLANDS  END_MIDLANDS  ERODED_BADLANDS  FLOWER_FOREST  FOREST  FROZEN_OCEAN  FROZEN_PEAKS  FROZEN_RIVER  GROVE  ICE_SPIKES  JAGGED_PEAKS  JUNGLE  LUKEWARM_OCEAN  LUSH_CAVES  MANGROVE_SWAMP  MEADOW  MUSHROOM_FIELDS  NETHER_WASTES  OCEAN  OLD_GROWTH_BIRCH_FOREST  OLD_GROWTH_PINE_TAIGA  OLD_GROWTH_SPRUCE_TAIGA  PLAINS  RIVER  SAVANNA  SAVANNA_PLATEAU  SMALL_END_ISLANDS  SNOWY_BEACH  SNOWY_PLAINS  SNOWY_SLOPES  SNOWY_TAIGA  SOUL_SAND_VALLEY  SPARSE_JUNGLE  STONY_PEAKS  STONY_SHORE  SUNFLOWER_PLAINS  SWAMP  TAIGA  THE_END  THE_VOID  WARM_OCEAN  WARPED_FOREST  WINDSWEPT_FOREST  WINDSWEPT_GRAVELLY_HILLS  WINDSWEPT_HILLS  WINDSWEPT_SAVANNA  WOODED_BADLANDS  OTHERS".split(" "))
SOUNDS = set("ANCIENT_ALTAR_FINISH_SOUND ANCIENT_ALTAR_ITEM_CHECK_SOUND ANCIENT_ALTAR_ITEM_DROP_SOUND ANCIENT_ALTAR_ITEM_PICK_UP_SOUND ANCIENT_ALTAR_START_SOUND ANCIENT_PEDESTAL_ITEM_PLACE_SOUND ARMOR_FORGE_FINISH_SOUND ARMOR_FORGE_WORKING_SOUND AUTO_CRAFTER_GUI_CLICK_SOUND AUTO_CRAFTER_UPDATE_RECIPE AUTOMATED_PANNING_MACHINE_FAIL_SOUND AUTOMATED_PANNING_MACHINE_SUCCESS_SOUND BACKPACK_CLOSE_SOUND BACKPACK_OPEN_SOUND BEE_BOOTS_FALL_SOUND COMPOSTER_COMPOST_SOUND COMPRESSOR_CRAFT_CONTRACT_SOUND COMPRESSOR_CRAFT_EXTEND_SOUND COMPRESSOR_CRAFT_SOUND COOLER_CONSUME_SOUND CRUCIBLE_ADD_LAVA_SOUND CRUCIBLE_ADD_WATER_SOUND CRUCIBLE_BLOCK_BREAK_SOUND CRUCIBLE_GENERATE_LIQUID_SOUND CRUCIBLE_INTERACT_SOUND CRUCIBLE_PLACE_LAVA_SOUND CRUCIBLE_PLACE_WATER_SOUND DEBUG_FISH_CLICK_SOUND DIET_COOKIE_CONSUME_SOUND ELYTRA_CAP_IMPACT_SOUND ENCHANTMENT_RUNE_ADD_ENCHANT_SOUND ENDER_BACKPACK_OPEN_SOUND ENHANCED_CRAFTING_TABLE_CRAFT_SOUND EXPLOSIVE_BOW_HIT_SOUND EXPLOSIVE_TOOL_EXPLODE_SOUND FISHERMAN_ANDROID_FISHING_SOUND FLASK_OF_KNOWLEDGE_FILLUP_SOUND GPS_NETWORK_ADD_WAYPOINT GPS_NETWORK_CREATE_WAYPOINT GPS_NETWORK_OPEN_PANEL_SOUND GRIND_STONE_INTERACT_SOUND GUIDE_BUTTON_CLICK_SOUND GUIDE_CONTRIBUTORS_OPEN_SOUND GUIDE_LANGUAGE_OPEN_SOUND GUIDE_OPEN_SETTING_SOUND IGNITION_CHAMBER_USE_FLINT_AND_STEEL_SOUND INFUSED_HOPPER_TELEPORT_SOUND INFUSED_MAGNET_TELEPORT_SOUND IRON_GOLEM_ASSEMBLER_ASSEMBLE_SOUND JETBOOTS_THRUST_SOUND JETPACK_THRUST_SOUND JUICER_USE_SOUND LIMITED_USE_ITEM_BREAK_SOUND MAGIC_SUGAR_CONSUME_SOUND MAGIC_WORKBENCH_FINISH_SOUND MAGIC_WORKBENCH_START_ANIMATION_SOUND MAGICAL_EYE_OF_ENDER_USE_SOUND MINER_ANDROID_BLOCK_GENERATION_SOUND MINING_TASK_SOUND ORE_WASHER_WASH_SOUND PLAYER_RESEARCHING_SOUND PORTABLE_CRAFTER_OPEN_SOUND PORTABLE_DUSTBIN_OPEN_SOUND PRESSURE_CHAMBER_FINISH_SOUND PRESSURE_CHAMBER_WORKING_SOUND PROGRAMMABLE_ANDROID_SCRIPT_DOWNLOAD_SOUND SLIME_BOOTS_FALL_SOUND SMELTERY_CRAFT_SOUND SOULBOUND_RUNE_RITUAL_SOUND SPLINT_CONSUME_SOUND STOMPER_BOOTS_STOMP_SOUND TAPE_MEASURE_MEASURE_SOUND TELEPORT_SOUND TELEPORT_UPDATE_SOUND TELEPORTATION_MANAGER_OPEN_GUI TOME_OF_KNOWLEDGE_USE_SOUND VAMPIRE_BLADE_HEALING_SOUND VANILLA_AUTO_CRAFTER_UPDATE_RECIPE_SOUND VILLAGER_RUNE_TRANSFORM_SOUND VITAMINS_CONSUME_SOUND WIND_STAFF_USE_SOUND".split(" "))
RAINBOW_TYPES = set("GLASS_PANE, GLASS, STAINED_GLASS, STAINED_GLASS_PANE, WOOL, TERRACOTTA, CUSTOM, GLAZED_TERRACOTTA, TERRACOTTA_ALL".split(", "))
SIMPLE_MACHINES_TYPES = set(("ELECTRIC_SMELTERY ELECTRIC_FURNACE ELECTRIC_GOLD_PAN ELECTRIC_DUST_WASHER ELECTRIC_ORE_GRINDER ELECTRIC_INGOT_FACTORY ELECTRIC_INGOT_PULVERIZER CHARGING_BENCH TREE_GROWTH_ACCELERATOR ANIMAL_GROWTH_ACCELERATOR CROP_GROWTH_ACCELERATOR FREEZER CARBON_PRESS ELECTRIC_PRESS ELECTRIC_CRUCIBLE FODD_FABRICATOR HEATED_PRESSURE_CHAMBER AUTO_ENCHANTER AUTO_DISENCHANTER BOOK_BINDER AUTO_ANVIL AUTO_DRIER AUTO_BREWER REFINERY PRODUCT_COLLECTOR").split(" "))
PROTECTION_TYPES = set(("BEES", "RADIATION", "FLYING_INTO_WALL"))
ARMOR_LEVELS = ["LEATHER", "CHAINMAIL", "IRON", "DIAMOND", "GOLDEN", "NETHERITE"]
EFFECTS = set("ABSORPTION BAD_OMEN BLINDNESS CONDUIT_POWER DARKNESS DOLPHINS_GRACE FIRE_RESISTANCE GLOWING HASTE HEALTH_BOOST HERO_OF_THE_VILLAGE HUNGER INFESTED INSTANT_DAMAGE INSTANT_HEALTH INVISIBILITY JUMP_BOOST LEVITATION LUCK MINING_FATIGUE NAUSEA NIGHT_VISION OOZING POISON RAID_OMEN REGENERATION RESISTANCE SATURATION SLOW_FALLING SLOWNESS SPEED STRENGTH TRIAL_OMEN UNLUCK WATER_BREATHING WEAKNESS WEAVING WIND_CHARGED WITHER".split(" "))
ENCHANTMENTS = {"AQUA_AFFINITY", "BANE_OF_ARTHROPODS", "BINDING_CURSE", "BLAST_PROTECTION", "BREACH", "CHANNELING", "DENSITY", "DEPTH_STRIDER", "EFFICIENCY", "FEATHER_FALLING", "FIRE_ASPECT", "FIRE_PROTECTION", "FLAME", "FORTUNE", "FROST_WALKER", "IMPALING", "INFINITY", "KNOCKBACK", "LOOTING", "LOYALTY", "LUCK_OF_THE_SEA", "LURE", "MENDING", "MULTISHOT", "PIERCING", "POWER", "PROJECTILE_PROTECTION", "PROTECTION", "PUNCH", "QUICK_CHARGE", "RESPIRATION", "RIPTIDE", "SHARPNESS", "SILK_TOUCH", "SMITE", "SOUL_SPEED", "SWEEPING_EDGE", "SWIFT_SNEAK", "THORNS", "UNBREAKING", "VANISHING_CURSE", "WIND_BURST"}
BHELMETS = [level+"_HELMET" for level in ARMOR_LEVELS]
BCHESTPLATES = [level+"_CHESTPLATE" for level in ARMOR_LEVELS]
BLEGGINGS = [level+"_LEGGINGS" for level in ARMOR_LEVELS]
BBOOTS = [level+"_BOOTS" for level in ARMOR_LEVELS]

BHELMETS.append("TURTLE_HELMET")
BCHESTPLATES.append("ELYTRA")
NULL = "__MISSING_STRING_RSCCHECKER"
RADIATION_LEVELS = {"HIGH", "LOW", "MODERATE", "VERY_HIGH", "VERY_DEADLY", NULL}

saveditems = set()
parentsGroups = set()
normalGroups = set()
items = set()
DEFAULT_RECIPE = [{"material_type": "none"}]*9
machines_slots = {}
lateinit_recipe_type = {}
totalBug = 0
totalWarn = 0
i = "loading config"
position = "loading config"
r = range(1, 10)


def getTimeString() -> str:
    return datetime.now().strftime("%H:%M:%S")


def getUTCTimeString() -> str:
    return datetime.utcnow().strftime("UTC %Y-%m-%d %H:%M:%S")


def error(string, end="\n") -> None:
    if totalBug < config["MaxPrintBug"]:
        print(f"{color.red}[{getTimeString()}] [RSCChecker/Bug]: {string}{color.reset}", end=end)


def warn(string, end="\n") -> None:
    if totalWarn < config["MaxPrintWarn"]:
        print(f"{color.gold}[{getTimeString()}] [RSCChecker/Warn]: {string}{color.reset}", end=end)


def info(string, end="\n") -> None:
    print(f"{color.white}[{getTimeString()}] [RSCChecker/Info]: {string}{color.reset}", end=end)


def debug(string, end="\n") -> None:
    global config
    if config["enable-debug"]:
        print(f"{color.purple}[{getTimeString()}] [RSCChecker/Debug]: {string}{color.reset}", end=end)


def report(position, Warn=False) -> None:
    global config, totalBug, totalWarn, MaxBug, MaxWarn
    if Warn and totalWarn == MaxWarn:
        totalWarn += 1
        error(f"{totalWarn} At {position}:", end="\n")
        error("Warn printing quantity has reached the maximum!")
    elif Warn and totalWarn < MaxWarn:
        totalWarn += 1
        warn(f"{totalWarn} At {position}:", end="\n")
    elif totalBug == MaxBug:
        totalBug += 1
        error(f"{totalBug} At {position}:", end="\n")
        error("Bug printing quantity has reached the maximum!")
    elif totalBug < MaxBug:
        totalBug += 1
        error(f"{totalBug} At {position}:", end="\n")


def startWith(string, target) -> bool:
    if string[:len(target)] == target:
        return True
    return False


def getYamlContext(file) -> dict:
    try:
        result = yaml.load(file, Loader=yaml.FullLoader)
        if result is None:
            return {}
        return result
    except FileNotFoundError:
        error(f"{file} not found")
        return {}
    except PermissionError:
        error("Permission denied")
        return {}


def RewriteSlimefunItems() -> None:
    global config
    if config["SlimefunItemsPath"] == "default":
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, "..\\Slimefun\\Items.yml")
    else:
        file_path = config["SlimefunItemsPath"]
    with open("__SlimefunItems.yml", "w", encoding="utf-8") as file:
        file.write("\n")
    with open(file_path, "r", encoding="utf-8") as file:
        regNames = getYamlContext(file).keys()
    with open("__SlimefunItems.yml", "w", encoding="utf-8") as file:
        yaml.dump({"items": list(regNames)}, file, allow_unicode=True, encoding="utf-8")


def getSaveditems(addon) -> set:
    items = set()
    for root, dirs, files in os.walk(f"addons/{addon}/saveditems"):
        for file_name in files:
            if file_name.endswith(".yml"):
                file_name = os.path.basename(file_name)
                items.add(file_name[:-4])
    return items


def getSlimefunItems() -> list:
    with open("__SlimefunItems.yml", "r", encoding="utf-8") as file:
        sfItems = getYamlContext(file)
    return sfItems["items"]


def getVanillaItems() -> list:
    with open("__VanillaItems.yml", "r", encoding="utf-8") as file:
        mcItems = getYamlContext(file)
    return mcItems["items"]


def getScripts(addon) -> set:
    items = set()
    for root, dirs, files in os.walk(f"addons/{addon}/scripts"):
        for file_name in files:
            if file_name.endswith(".js"):
                file_name = os.path.basename(file_name)
                items.add(file_name[:-3])
    return items


def inSlimefun(item) -> bool:
    return item in SlimefunItems


def inVanilla(item) -> bool: 
    return item.upper() in VANILLA_ITEMS


def inSaveditems(item) -> bool: 
    return str(item) in saveditems


def inBiome(item) -> bool: 
    return item.upper() in BIOMES


def inScripts(item) -> bool: 
    return str(item) in scripts


def inSound(item) -> bool: 
    return item in SOUNDS


def inRainbowTypes(dtype) -> bool: 
    return dtype in RAINBOW_TYPES


def inHelmets(item) -> bool: 
    return item.upper() in BHELMETS


def inChestplates(item) -> bool: 
    return item.upper() in BCHESTPLATES


def inLeggings(item) -> bool: 
    return item.upper() in BLEGGINGS


def inBoots(item) -> bool: 
    return item.upper() in BBOOTS


def inEnchantments(item) -> bool: 
    return item.upper() in ENCHANTMENTS


def inRadiationLevels(item) -> bool: 
    return item.upper() in RADIATION_LEVELS


def isVanilla(item, position) -> None:
    if not inVanilla(item):
        report(position)
        error(f"{item} is not a valid vanilla item")


def isSlimefun(item, position) -> None:
    if not inSlimefun(item) and item not in items:
        report(position)
        error(f"{item} is not a valid Slimefun item")


def isSaveditem(item, position) -> None:
    if not inSaveditems(str(item)):
        report(position)
        error(f"{item} is not a valid saveditem")


def isBiome(item, position) -> None:
    if not inBiome(item):
        report(position)
        error(f"{item} is not a valid biome")


def isSound(item, position) -> None:
    if not inSound(item):
        report(position)
        error(f"{item} is not a valid sound")


def isScript(item, position) -> None:
    if item == NULL:
        return
    if not inScripts(item):
        report(position)
        error(f"{item} is not a valid script")


def isRainbowType(dtype, position) -> None:
    if not inRainbowTypes(dtype):
        report(position+".rainbow")
        error(f"{dtype} is not a valid rainbow type")


def isHelmet(item, position) -> None:
    if not inHelmets(item):
        report(position)
        error(f"{item} is not a valid helmet")


def isChestplate(item, position) -> None:
    if not inChestplates(item):
        report(position)
        error(f"{item} is not a valid chestplate")


def isLeggings(item, position) -> None:
    if not inLeggings(item):
        report(position)
        error(f"{item} is not a valid leggings")


def isBoots(item, position) -> None:
    if not inBoots(item):
        report(position)
        error(f"{item} is not a valid boots")


def isEnchantment(item, position) -> None:
    if not inEnchantments(item):
        report(position)
        error(f"{item} is not a valid enchantment")


def isInt(num, position, bottom=0, top=MAXINT, Warn=False) -> None:
    if isinstance(num, int):
        if not bottom <= num <= top:
            if Warn:
                report(position, Warn)
                warn(f"{num} is not in range [{bottom},{top}]")
            else:
                report(position)
                error(f"{num} is not in range [{bottom},{top}]")
    else:
        report(position)
        error("arugment must be an integer!")


def isBool(item, position) -> None:
    if not ((item is True) or (item is False)):
        report(position)
        error("arugment must be a boolean!")


def isList(item, position) -> None:
    if not isinstance(item, list):
        report(position)
        error("arugment must be a list!")


def isDict(item, position) -> None:
    if not isinstance(item, dict):
        report(position)
        error("argument must be a dict!")


def isMap(item, position) -> None:
    if not isinstance(item, map):
        report(position)
        error("argument must be a map!")


def isRadiationLevel(item, position) -> None:
    if not inRadiationLevels(item):
        report(position)
        error(f"{item} is not a valid radiation level")


def getItemMaxStack(item) -> int:
    return MaxStacks[item.upper()]


def isAmountProper(item, dAm, position, zero=False, warn=False) -> None:
    isInt(dAm, f"{position}", -1, 64, warn)


def isItem(data, position, Warn=False) -> None:
    # necessary
    dtype = data.get("material_type", "mc")
    did = data.get("material", "STONE")
    if dtype == "mc":
        isVanilla(did, position+".material_type")
    elif dtype == "slimefun":
        isSlimefun(did, position+".material_type")
    elif dtype == "saveditem":
        isSaveditem(did, position+".material_type")
    elif did == NULL and dtype != "none":
        report(position)
        error("Excepted argument 'material' but got none")
    elif dtype not in ("none", "skull_base64", "skull_url", "skull_hash"):
        report(position+".material_type")
        error('type must be "mc", "slimefun", "saveditem", "none", "skull_base64", "skull_url" or "skull_hash"！')
    if dtype != "none":
        dam = data.get("amount", 1)
        isAmountProper(did, dam, position+".amount", warn=Warn)

    # not necessary
    dmodelid = data.get("modelId", 0)
    isInt(dmodelid, position)


def isRecipe(data, position) -> None:
    recipe_type = data.get("recipe_type", NULL)
    recipe = DEFAULT_RECIPE
    load_recipe = data.get("recipe", {})
    for bvar in load_recipe:
        if bvar in r:
            isItem(load_recipe[bvar], f"{position}.{bvar}")
            item = load_recipe.get("material", NULL)
            recipe[bvar-1] = {
                "material": item,
                "material_type": load_recipe.get("material_type", "mc" if item != NULL else "none"),
                "amount": load_recipe.get("amount", 1)
            }
        else:
            report(position, True)
            warn(f"{bvar} is not a valid variable in recipe")
    if recipe_type == NULL:
        if recipe != DEFAULT_RECIPE:
            report(position)
            error("Excepted argument 'recipe_type' but got none")
        else:
            recipe_type = "NULL"
    else:
        isRecipeType(recipe_type, position)
    idx = 1
    if recipe_type in {"ENHANCED_CRAFTING_TABLE", "MAGIC_WORKBENCH", "ARMOR_FORGE", "PRESSURE_CHAMBER"}:
        for k in recipe:
            if k["material_type"] != "none" and k["amount"] != 1:
                report(position+f".crafting-recipe.{idx}")
                error(f"Slot {idx}'s amount must be 1")
            idx += 1
    elif recipe_type in {"COMPRESSOR", "PRESSURE_CHAMBER", "ORE_CRUSHER", "GRIND_STONE"}:
        for k in recipe[1:]:
            if k["material_type"] != "none" and k["material"] != NULL:
                report(position+f".crafting-recipe.{idx}")
                error(f"Slot {idx} must be none type")
            idx += 1
    elif recipe_type == "ANCIENT_ALTAR":
        for k in recipe:
            if k["material_type"] == "none" and k["material"] != NULL:
                report(position+f".crafting-recipe.{idx}.type")
                error(f"Slot {idx} must be not none type")
            if k["material_type"] != "none" and k["amount"] != 1:
                report(position+f".crafting-recipe.{idx}.type")
                error(f"Slot {idx}'s amount must be 1")
            idx += 1
    elif recipe_type == "SMELTERY":
        sum_dict = {}
        for k in recipe:
            if k["material_type"] == "none":
                continue
            key = k["material"]
            value = k["amount"]
            if key in sum_dict:
                sum_dict[key] += value
                if sum_dict[key] > 64:
                    report(position+f".{idx}.amount")
                    error("{key}'s amount must be less than or equal to 64")
                    break
            else:
                sum_dict[key] = value
            idx += 1


def isLateInit(data) -> bool:
    return data.get("lateInit", False)


def loadReg(data, position) -> None:
    # not necessary
    dlateinit = isLateInit(data)
    isBool(dlateinit, position+".lateInit")
    dreg = data.get("register", {})
    warn = dreg.get("warn", False)
    isBool(warn, position+".warn")
    cond = dreg.get("conditions", ["version > 1.20"])
    for dat in cond:
        if startWith(dat, "version"):
            temp = dat.split(" ")
            if len(temp) != 3:
                report(position+".conditions")
                error(f"Wrong arugment amount in ' {dat} '")
            elif temp[1] in (">=", "<=", ">", "<"):
                for i in temp[2].split("."):
                    isInt(int(i), position)
            else:
                report(position+".conditions")
                error("Compare operator must be '>=', '<=', '>' or '<'")
    unfinished = dreg.get("unfinished", False)
    isBool(unfinished, position+".unfinished")


def isGroup(group, position) -> None:
    if group not in normalGroups:
        report(position, True)
        warn(f"{group} may not a valid group")


def isRecipeType(recipe_type, position) -> None:
    if recipe_type not in RECIPE_TYPES:
        lateinit_recipe_type[position] = recipe_type


def inSlots(name, slots, position, status_slot=-1) -> None:
    ms = machines_slots.get(name, NULL)
    if ms == NULL:
        return
    for slot in slots:
        isInt(slot, position, 0, 53)
        if slot in ms:
            report(position)
            error("Bad slot number, it is already used.")
        if slot == status_slot:
            report(position)
            error(f"Slot {status_slot} is alread used for status")


def slot_read(slots, position) -> set:
    fs = set()
    for j in slots:
        if isinstance(j, int):
            if j in fs:
                report(position, True)
                warn("Bad slot number, it is already used.")
            else:
                fs.add(j)
        elif isinstance(j, str):
            rang = j.split("-")
            if len(rang) == 2:
                for n in range(int(rang[0]), int(rang[1])):
                    if n in fs:
                        report(position, True)
                        warn("Bad slot number, it is already used.")
                    else:
                        fs.add(n)
            else:
                report(position)
                error(f"{rang} may not a valid slot range")
        else:
            report(position)
            error(f"{j} must be an integer or a slot range")
    return fs


def checkPotionEffects(data) -> None:
    global i, position
    potion_effects = data.get("potion_effects", [])
    for string in potion_effects:
        position = f"{position}.potion_effects.'{string}'"
        split = string.split(" ")
        if len(split) != 2:
            report(position)
            error("Wrong potion effect format, should be 'SPEED 5'")
            continue
        effect = split[0]
        amp = int(split[1])
        if effect not in EFFECTS:
            report(position)
            error(f"{effect} is not a valid potion effect")
        if amp < 0:
            report(position)
            error(f"{amp} must be a positive integer")


def checkGroups(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        position = f"groups: {scan_file}.{i}"
        loadReg(data, position)
        isItem(data["item"], position+".item")
        dtype = data.get("type", "normal")
        if dtype in {"nested", "parent"}:
            parentsGroups.add(i)
        elif dtype == "sub":
            normalGroups.add(i)
            parent = data.get("parent", NULL)
            if parent == NULL:
                report(position)
                error("Expected argument 'parent' but got none")
            elif parent not in parentsGroups:
                report(position+".parent")
                error(f"{parent} is not a valid nested group")
        elif dtype == "seasonal":
            normalGroups.add(i)
            month = data["month"]
            isInt(month, position+".month", 1, 12)
        elif dtype == "locked":
            normalGroups.add(i)
        elif dtype == "normal":
            normalGroups.add(i)
        else:
            report(position)
            error("type must be 'nested', 'parent', 'sub', 'seasonal', 'locked' or 'normal'")
        dtier = data.get("tier", 1)
        isInt(dtier, position+".tier", -1)

    lateinits = set()
    scan_file = "addons/"+addon+"/groups.yml"
    info(f"Loading groups: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        if k[i].get("type", "normal") in {"nested", "parent"}:
            parentsGroups.add(i)
        else:
            normalGroups.add(i)
    yield
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


def checkRecipeTypes(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        position = f"RECIPE_TYPES: {scan_file}.{i}"
        loadReg(data, position)
        isItem(data, position+".item")
        RECIPE_TYPES.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/RECIPE_TYPES.yml"
    info(f"Loading RECIPE_TYPES: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        RECIPE_TYPES.add(i)
    yield
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


def checkMobDrops(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        # necessary
        position = f"mob_drops: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        dentity = data["entity"]
        if dentity not in entities:
            report(position+".entity")
            error(f"{dentity} is not a valid entity")
        dchance = data["chance"]
        isInt(dchance, position+".chance", 0, 100)
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/mob_drops.yml"
    info(f"Loading mob_drops: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
    
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


def checkGeoResources(addon) -> Generator[Any, Any, Any]:
    global i, position

    def check(data) -> None:
        global i, position
        # necessary
        position = f"geo_resources: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        drecipe_type = data.get("recipe_type")
        isRecipeType(drecipe_type, position+".recipe_type")
        dmax_deviation = data["max_deviation"]
        isInt(dmax_deviation, position+".max_deviation")
        dobtain_from_geo_miner = data["obtain_from_geo_miner"]
        isBool(dobtain_from_geo_miner, position+".obtain_from_geo_miner")
        supply = data["supply"]
        flag = True
        position +=".supply"
        for e in supply:
            if e in ("normal", "nether", "the_end"):
                env = supply[e]
                if isinstance(env, dict):
                    for biome in env:
                        isBiome(biome, position+f".{e}")
                        isInt(env[biome], position+f".{e}.{biome}")
                elif isinstance(env, int):
                    isInt(env, position+f".{e}")
                else:
                    report(position)
                    error("Wrong format of supply")
                flag = False
        if flag:
            report(position, True)
            warn("supply.world must be 'normal' or 'nether' or 'the_end'")
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/geo_resources.yml"
    info(f"Loading geo_resources: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield    
    

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


def checkItems(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        # necessary
        position = f"items: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        isRecipe(data, position+".recipe")
        
        # not necessary
        dplaceable = data.get("placeable", False)
        isBool(dplaceable, position+".placeable")
        dscript = data.get("script", NULL)
        isScript(dscript, position+".script")
        dglow = data.get("glow", False)
        isBool(dglow, position+".glow")
        drainbow = data.get("rainbow", "WOOL")
        isRainbowType(drainbow, position+".rainbow.{ritem}")
        if drainbow == "CUSTOM":
            rainbow_materials = data.get("rainbow_materials", NULL)
            if rainbow_materials == NULL:
                report(position)
                error("Expected argument 'rainbow_materials' but got none")
            for ritem in rainbow_materials:
                isVanilla(ritem, position+".rainbow_materials")
        danti_wither = data.get("anti_wither", False)
        isBool(danti_wither, position+".anti_wither")
        dsoulbound = data.get("soulbound", False)
        isBool(dsoulbound, position+".soulbound")
        dvanilla = data.get("vanilla", False)
        isBool(dvanilla, position+".vanilla")
        energy_capacity = data.get("energy_capacity", 0)
        isInt(energy_capacity, position+".energy_capacity")
        radiation = data.get("radiation", NULL)
        if radiation not in RADIATION_LEVELS:
            report(position+".radiation")
            error(f"{radiation} is not a valid radiation level")
        piglin_trade_chance = data.get("piglin_trade_chance", 0)
        isInt(piglin_trade_chance, position+".piglin_trade_chance")
        hidden = data.get("hidden", False)
        isBool(hidden, position+".hidden")
        denchantments = data.get("ENCHANTMENTS", {})
        for denchantment, dlevel in denchantments.items():
            isEnchantment(denchantment, position+".ENCHANTMENTS")
            isInt(dlevel, position+".ENCHANTMENTS."+denchantment, 0, 255)
        drop_from = data.get("drop_from", NULL)
        if drop_from != NULL:
            isVanilla(drop_from, position)
            drop_amount = data.get("drop_amount", 1)
            drop_chance = data.get("drop_chance", 100)
            isInt(drop_amount, position+".drop_amount", 1, 64)
            isInt(drop_chance, position+".drop_chance", 1, 64)
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/items.yml"
    info(f"Loading items: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkArmors(addon) -> Generator[Any, Any, Any]:
    global i, position

    def check(data) -> None:
        global i, position
        position = f"armors: {scan_file}.{i}"
        loadReg(data, position)
        fullset = data.get("fullSet", False)
        isBool(fullset, position+".fullSet")
        item_group = data["item_group"]
        isGroup(item_group, position+".item_group")
        dpts = data["PROTECTION_TYPES"]
        for dpt in dpts:
            if dpt not in PROTECTION_TYPES:
                report(position+".PROTECTION_TYPES")
                error(f"{dpt} is not a valid protection type")

        helmet = data.get("helmet", NULL)
        chestplate = data.get("chestplate", NULL)
        leggings = data.get("leggings", NULL)
        boots = data.get("boots", NULL)
        if NULL == helmet == chestplate == leggings == boots:
            report(position)
            error("Excepted any armor parts but got none")
        if helmet != NULL:
            isRecipe(helmet, position)
            isHelmet(helmet["material"], position+".material")
            checkPotionEffects(helmet)
            items.add(helmet["id"])
        if chestplate != NULL:
            isRecipe(chestplate, position)
            isChestplate(chestplate["material"], position+".material")
            checkPotionEffects(chestplate)
            items.add(chestplate["id"])
        if leggings != NULL:
            isRecipe(leggings, position)
            isLeggings(leggings["material"], position+".material")
            checkPotionEffects(leggings)
            items.add(leggings["id"])
        if boots != NULL:
            isRecipe(boots, position)
            isBoots(boots["material"], position+".material")
            checkPotionEffects(boots)
            items.add(boots["id"])

    lateinits = set()
    scan_file = "addons/"+addon+"/armors.yml"
    info(f"Loading armors: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        data = k[i]
        helmet = data.get("helmet", NULL)
        chestplate = data.get("chestplate", NULL)
        leggings = data.get("leggings", NULL)
        boots = data.get("boots", NULL)
        if helmet != NULL:
            items.add(helmet["id"])
        if chestplate != NULL:
            items.add(chestplate["id"])
        if leggings != NULL:
            items.add(leggings["id"])
        if boots != NULL:
            items.add(boots["id"])
    yield
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


def checkCapacitors(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        position = f"capacitors: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        dcapacity = data["capacity"]
        isInt(dcapacity, position+".capacity", 1)
        isRecipe(data, position+".recipe")
        items.add(i)
        
    lateinits = set()
    scan_file = "addons/"+addon+"/capacitors.yml"
    info(f"Loading capacitors: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkFoods(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        # necessary
        position = f"foods: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        isRecipe(data, position+".recipe")
        
        # not necessary
        dplaceable = data.get("placeable", False)
        isBool(dplaceable, position+".placeable")
        dscript = data.get("script", NULL)
        isScript(dscript, position+".script")
        if dscript == NULL:
            report(position)
            error("Excepted a script in foods.yml but got none")
        dglow = data.get("glow", False)
        isBool(dglow, position+".glow")
        drainbow = data.get("rainbow", "WOOL")
        isRainbowType(drainbow, position+".rainbow.{ritem}")
        if drainbow == "CUSTOM":
            rainbow_materials = data.get("rainbow_materials", NULL)
            if rainbow_materials == NULL:
                report(position)
                error("Expected argument 'rainbow_materials' but got none")
            for ritem in rainbow_materials:
                isVanilla(ritem, position+".rainbow_materials")
        danti_wither = data.get("anti_wither", False)
        isBool(danti_wither, position+".anti_wither")
        dsoulbound = data.get("soulbound", False)
        isBool(dsoulbound, position+".soulbound")
        dvanilla = data.get("vanilla", False)
        isBool(dvanilla, position+".vanilla")
        energy_capacity = data.get("energy_capacity", 0)
        isInt(energy_capacity, position+".energy_capacity")
        radiation = data.get("radiation", NULL)
        isRadiationLevel(radiation, position+".radiation")
        piglin_trade_chance = data.get("piglin_trade_chance", 0)
        isInt(piglin_trade_chance, position+".piglin_trade.piglin_trade_chance")

        items.add(i)
    
    lateinits = set()
    scan_file = "addons/"+addon+"/foods.yml"
    info(f"Loading foods: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkMenus(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        position = f"menus: {scan_file}.{i}"
        loadReg(data, position)
        dimport = data.get("import", NULL)
        if dimport == NULL:
            dtitle = data.get("title", NULL)
            if dtitle == NULL:
                report(position+".title")
                error("缺少 title！")
            slots = data["slots"]
            for slot in slots:
                s = slots[slot]
                isItem(s, position+f".{slot}")
                progressbar = s.get("progressbar", False)
                isBool(progressbar, position+".progressbar")
            machines_slots[i] = slot_read(slots, position+".slots")
        else:
            if dimport not in machines_slots:
                report(position+".import", True)
                warn(f"{dimport} may not a valid machine")

    lateinits = set()
    scan_file = "addons/"+addon+"/menus.yml"
    info(f"Loading menus: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        machines_slots[i] = []

    yield
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


def checkMachines(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        # necessary
        position = f"machines: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        isRecipe(data, position+".recipe")
        work = data.get("work", -1)
        isInt(work, position+".work", -1, 53)
        ioput = data["input"] + data["output"]
        inSlots(i, ioput, position+".input/output", work)

        # not necessary
        dscript = data.get("script", NULL)
        isScript(dscript, position+".script")
        energy = data.get("energy", NULL)
        position +=".energy"
        if energy != NULL:
            dcapacity = energy.get("capacity", 0)
            isInt(dcapacity, position+".capacity")
            dtotalticks = energy["totalTicks"]
            isInt(dtotalticks, position+".totalTicks", 1)
            dtype = energy.get("type", "NONE")
            if dtype not in ("CAPACITOR", "CONNECTOR", "CONSUMER", "GENERATOR", "NONE"):
                report(position+".type")
                error("type must be CAPACITOR, CONNECTOR, CONSUMER, GENERATOR or NONE")
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/machines.yml"
    info(f"Loading machines: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkGenerators(addon) -> Generator[Any, Any, Any]:
    global i, position

    def check(data) -> None:
        global i, position
        # necessary
        position = f"generators: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        isRecipe(data, position+".recipe")
        ioput = data["input"] + data["output"]
        inSlots(i, ioput, position+".input/output")
        dcapacity = data.get("capacity", 0)
        isInt(dcapacity, position+".capacity")
        dproduction = data["production"]
        isInt(dproduction, position+".production", 1)
        fuels = data["fuels"]
        position +=".fuels"
        for ddk in fuels:
            recipe = fuels[ddk]
            item = recipe.get("item", {})
            isItem(item, position+f".{ddk}.item")
            seconds = recipe["seconds"]
            isInt(seconds, position+f".{ddk}.seconds", 0)
            output = recipe.get("output", {})
            isItem(output, position+f".{ddk}.output")
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/generators.yml"
    info(f"Loading generators: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkSolarGenerators(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        # necessary
        position = f"solar_generators: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        isRecipe(data, position+".recipe")
        dcapacity = data["capacity"]
        isInt(dcapacity, position+".capacity", 1)
        dday = data["dayEnergy"]
        isInt(dday, position+".dayEnergy", 1)
        dnight = data["nightEnergy"]
        isInt(dnight, position+".nightEnergy", 1)
        dlight = data["lightLevel"]
        isInt(dlight, position+".lightLevel", 0, 15)
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/solar_generators.yml"
    info(f"Loading solar_generators: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkMaterialGenerators(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        # necessary
        position = f"mat_generators: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        isRecipe(data, position+".recipe")
        dcapacity = data["capacity"]
        isInt(dcapacity, position+".capacity", 1)
        outputItem = data["outputItem"]
        isItem(outputItem, position+".outputItem", Warn=True)
        tickrate = data["tickRate"]
        isInt(tickrate, position+".tickRate", 1)
        status_slot = data["status"]
        isInt(status_slot, position+".status", 0, 53)
        output = data["output"]
        inSlots(i, output, position+".output", status_slot)
        per = data["per"]
        isInt(per, position+".per", 1)
        items.add(i)
    
    lateinits = set()
    scan_file = "addons/"+addon+"/mat_generators.yml"
    info(f"Loading mat_generators: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkRecipeMachines(addon) -> Generator[Any, Any, Any]:
    global i, position

    def check(data) -> None:
        global i, position
        # necessary
        position = f"recipe_machines: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        isRecipe(data, position+".recipe")
        dinput = data["input"]
        doutput = data["output"]
        ioput = dinput + doutput
        inSlots(i, ioput, position+".input/output")
        dcapacity = data["capacity"]
        isInt(dcapacity, position+".capacity", 0)
        depc = data["energyPerCraft"]
        isInt(depc, position+".energyPerCraft", 1)
        speed = data.get("speed", 1)
        isInt(speed, position+".speed", 1)
        leninput = len(dinput)
        lenoutput = len(doutput)
        recipes = data["recipes"]
        position +=".recipes"
        BP = position
        for key, recipe in recipes.items():
            position = BP + f".{key}"
            seconds = recipe["seconds"]
            isInt(seconds, position+".seconds", 0)
            chooseOne = recipe.get("chooseOne", False)
            isBool(chooseOne, position+".chooseOne")
            temp = {}
            types = []
            recipe_input = recipe.get("input", {})
            if len(recipe_input) > leninput:
                report(position+".input")
                error("Bad recipe input, not enough slots")
            for o in recipe_input:
                ri = recipe_input[o]
                itype = ri.get("material_type", "mc")
                isItem(ri, position+f".input.{o}")
                key = (ri["material"], itype)
                if key in temp:
                    temp[key] += 1
                else:
                    temp[key] = 1
                types.append(itype)
            for p in temp.values():
                if p > 1:
                    report(position+".input")
                    error("You cannot have the same material in the recipe input more than once")
                    error("According to Slimefun Github Issue #4166.")
            for p in types:
                if types[0] == "none":
                    report(position+".input")
                    error("Cannot set material_type to none for first item")
            temp = {}
            recipe_output = recipe.get("output", {})
            if len(recipe_output) > lenoutput:
                report(position+".output")
                error("Bad recipe output, not enough slots")
            for o in recipe_output:
                ro = recipe_output[o]
                itype = ro.get("material_type", "mc")
                isItem(ro, position+f".output.{o}")
                key = (ro["material"], itype)
                if key in temp:
                    temp[key] += 1
                else:
                    temp[key] = 1
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/recipe_machines.yml"
    info(f"Loading recipe_machines: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkSimpleMachines(addon) -> Generator[Any, Any, Any]:
    global i, position

    def check(data) -> None:
        global i, position
        # necessary
        position = f"simple_machines: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        isRecipe(data, position+".recipe")
        dtype = data["type"]
        if dtype not in SIMPLE_MACHINES_TYPES:
            report(position+".type")
            error(f"{dtype} is not a valid type")
        settings = data["settings"]
        position +=".settings"
        dcapacity = settings["capacity"]
        isInt(dcapacity, position+".capacity", 1)
        dconsumption = settings["consumption"]
        isInt(dconsumption, position+".consumption", 1)
        dspeed = settings.get("speed", 1)
        isInt(dspeed, position+".speed", 1)
        dradius = settings.get("radius", 1)
        isInt(dradius, position+".radius", 1)
        drepair = settings.get("repair_factor", 10)
        isInt(drepair, position+".repair_factor", 1)
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/simple_machines.yml"
    info(f"Loading simple_machines: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkMultiblockMachines(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        # necessary
        position = f"mb_machines: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        recipe = data["recipe"]
        hasdispenser = False
        for key, avar in recipe.items():
            dtype = avar.get("material_type", "mc")
            if dtype != "mc":
                report(position+f".{key}.type", True)
                warn("Block material must be vanilla")
            material = avar["material"]
            if material in ("DISPENSER", "dispenser"):
                hasdispenser = True
        if not hasdispenser:
            report(position+".recipe")
            error("Dispenser is required in recipe")
        work = data["work"]
        isInt(work, position+".work", 1, 9)
        sound = data["sound"]
        isSound(sound, position+".sound")
        recipes = data["recipes"]
        position +=".recipes"
        for recipe in recipes.values():
            recipe_input = recipe["input"]
            if len(recipe_input) > 9:
                report(position+".input")
                error("Bad recipe input, not enough slots")
            for o in recipe_input:
                ri = recipe_input[o]
                isItem(ri, position+f".input.{o}")
            recipe_output = recipe["output"]
            isItem(recipe_output, position+".output")
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/mb_machines.yml"
    info(f"Loading mb_machines: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkSupers(addon) -> Generator[Any, Any, Any]:
    global i, position
    
    def check(data) -> None:
        global i, position
        # necessary
        position = f"supers: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        isRecipe(data, position+".recipe")
        dclass = data["class"]
        if not isinstance(dclass, str):
            report(position)
            error(f"{dclass} is not a valid class")
        # not necessary
        dargs = data.get("args", [])
        if not isinstance(dargs, list):
            report(position+".args")
            error("args must be a list")
        dctor = data.get("ctor", 0)
        isInt(dctor, position+".dctor")
        darg_template = data.get("arg_template", [])
        isList(darg_template, position+".arg_template")
        dmethod = data.get("method", {})
        isDict(dmethod, position+".method")
        dfield = data.get("field", {})
        isDict(dfield, position+".field")
        items.add(i)
    
    lateinits = set()
    scan_file = "addons/"+addon+"/supers.yml"
    info(f"Loading supers: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkTemplateMachines(addon) -> Generator[Any, Any, Any]:
    global i, position

    def check(data) -> None:
        global i, position
        # necessary
        position = f"template_machines: {scan_file}.{i}"
        loadReg(data, position)
        dgroup = data["item_group"]
        isGroup(dgroup, position+".item_group")
        ditem = data["item"]
        isItem(ditem, position+".item")
        isRecipe(data, position+".recipe")
        dconsumption = data["consumption"]
        isInt(dconsumption, position+".consumption", 1)
        dcapacity = data["capacity"]
        isInt(dcapacity, position+".capacity", 1)
        dtemplateSlot = data["template_slot"]
        isInt(dtemplateSlot, position+".template_slot", 0, 53)
        dinput = data["input"]
        doutput = data["output"]
        ioput = dinput + doutput
        inSlots(i, ioput, position+".input/output")
        dfasterIfMoreTemplates = data.get("fasterIfMoreTemplates", False)
        isBool(dfasterIfMoreTemplates, position+".fasterIfMoreTemplates")
        dmoreOutputIfMoreTemplates = data.get("moreOutputIfMoreTemplates", False)
        isBool(dmoreOutputIfMoreTemplates, position+".moreOutputIfMoreTemplates")
        drecipes = data["recipes"]
        leninput = len(dinput)
        lenoutput = len(doutput)
        position += ".recipes"
        BP = position
        for key in drecipes:
            BP = position + f".{key}"
            isSlimefun(key, position)
            recipe = drecipes[key]
            for r in recipe:
                BP += f".{r}"
                rec = recipe[r]
                dseconds = rec.get("seconds", 0)
                isInt(dseconds, position+f".{key}.{r}.seconds", 0)
                recipe_input = rec.get("input", {})
                temp = {}
                types = []
                if len(recipe_input) > leninput:
                    report(position+".input")
                    error("Bad recipe input, not enough slots")
                for o in recipe_input:
                    ri = recipe_input[o]
                    itype = ri.get("material_type", "mc")
                    isItem(ri, position+f".input.{o}")
                    key = (ri["material"], itype)
                    if key in temp:
                        temp[key] += 1
                    else:
                        temp[key] = 1
                    types.append(itype)
                for p in temp.values():
                    if p > 1:
                        report(position+".input")
                        error("You cannot have the same material in the recipe input more than once")
                        error("According to Slimefun Github Issue #4166.")
                for p in types:
                    if types[0] == "none":
                        report(position+".input")
                        error("Cannot set material_type to none for first item")
                temp = {}
                recipe_output = rec.get("output", {})
                if len(recipe_output) > lenoutput:
                    report(position+".output")
                    error("Bad recipe output, not enough slots")
                for o in recipe_output:
                    ro = recipe_output[o]
                    itype = ro.get("material_type", "mc")
                    isItem(ro, position+f".output.{o}")
                    key = (ro["material"], itype)
                    if key in temp:
                        temp[key] += 1
                    else:
                        temp[key] = 1
        items.add(i)

    lateinits = set()
    scan_file = "addons/"+addon+"/template_machines.yml"
    info(f"Loading template_machines: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    for i in k:
        items.add(i)
    
    yield
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


def checkResearches(addon) -> Generator[Any, Any, Any]:
    global i, position

    def check(data) -> None:
        global i, position
        # necessary
        position = f"researches: {scan_file}.{i}"
        loadReg(data, position)
        did = data["id"]
        isInt(did, position+".id")
        for item in data["items"]:
            isSlimefun(item, position+".items")

        # special
        dlc = data.get("levelCost", NULL)
        dcc = data.get("currencyCost", NULL)
        flag = True
        if dlc != NULL:
            isInt(dlc, position+".levelCost", 1)
            flag = False
        if dcc != NULL:
            isInt(dcc, position+".currencyCost", 1)
            flag = False
        if flag:
            report(position)
            error("Excepcted levelCost/currencyCost but not found")

    lateinits = set()
    scan_file = "addons/"+addon+"/researches.yml"
    info(f"Loading researches: {scan_file}")
    with open(scan_file, "r", encoding="utf-8") as f:
        k = getYamlContext(f)
        if not isinstance(k, dict):
            report(scan_file)
            error("Cannot read any available content!")
            yield
            yield
            yield


    # preload
    yield
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


def checkAll() -> None:
    global i, position, saveditems, scripts
    for addon in addons:
        info(f"{color.green}Loading Addon {addon}")
        chs = []
        scripts = getScripts(addon)
        saveditems = getSaveditems(addon)
        for checker in checkers:
            if checker == int:
                continue
            chs.append(checker(addon))
        for __ in range(3):
            if __ == 0:
                info(f"{color.gold}Preloading items:")
            if __ == 1:
                info(f"{color.gold}Loading normal items:")
            if __ == 2:
                info(f"{color.gold}Loading lateInit items:")
            for ch in chs:
                start = time()
                try:
                    info(f"Start task {ch.__name__}")
                    next(ch)
                except (yaml.scanner.ScannerError, yaml.parser.ParserError) as err:
                    error("Seems some wrong in YAML file, please check it")
                    error("https://www.bejson.com/validators/yaml_editor/")
                    error(err)
                except FileNotFoundError as ignored:
                    warn("File not found and pass")
                except KeyError as err:
                    error("Cannot find the key")
                    error(err)
                except StopIteration as ignored:
                    ...
                info(f"{color.green}Done task {ch.__name__} in {round(time() - start, 3)}s")


try:
    sum_start = time()
    info(f"""{color.cyan}
    ,-.----.    .--.--.     ,----..              ,---,                              ,-.                     
    \    /  \  /  /    '.  /   /   \           ,--.' |                          ,--/ /|                     
    ;   :    \|  :  /`. / |   :     :          |  |  :                        ,--. :/ |             __  ,-. 
    |   | .\ :;  |  |--`  .   |  ;. /          :  :  :                        :  : ' /            ,' ,'/ /| 
    .   : |: ||  :  ;_    .   ; /--`    ,---.  :  |  |,--.   ,---.     ,---.  |  '  /      ,---.  '  | |' | 
    |   |  \ : \  \    `. ;   | ;      /     \ |  :  '   |  /     \   /     \ '  |  :     /     \ |  |   ,' 
    |   : .  /  `----.   \|   : |     /    / ' |  |   /' : /    /  | /    / ' |  |   \   /    /  |'  :  /   
    ;   | |  \  __ \  \  |.   | '___ .    ' /  '  :  | | |.    ' / |.    ' /  '  : |. \ .    ' / ||  | '    
    |   | ;\  \/  /`--'  /'   ; : .'|'   ; :__ |  |  ' | :'   ;   /|'   ; :__ |  | ' \ \'   ;   /|;  : |    
    :   ' | \.'--'.     / '   | '/  :'   | '.'||  :  :_:,''   |  / |'   | '.'|'  : |--' '   |  / ||  , ;    
    :   : :-'   `--'---'  |   :    / |   :    :|  | ,'    |   :    ||   :    :;  |,'    |   :    | ---'     
    |   |.'                \   \ .'   \   \  / `--''       \   \  /  \   \  / '--'       \   \  /           
    `---'                   `---`      `----'               `----'    `----'              `----'
    {color.reset}""")
    info(f"{color.cyan}RSCchecker {color.green}{_VERSION}")
    info(f"{color.cyan}Developed by guguguhello")
    info(f"{color.cyan}Using Version: {color.green}{_VERSION}")
    info(f"{color.cyan}Repo: {color.green}https://github.com/SlimefunReloadingProject/RSCchecker")
    info(f"{color.cyan}Current Time: {color.green}{getTimeString()}")
    info(f"{color.cyan}UTC Time: {color.green}{getUTCTimeString()}")
    info(REPORT_BUGS)
    info(BIG_THANKS)
    info(f"{color.cyan}Loading config")
    with open("RSCchecker-config.yml", "r", encoding="utf-8") as file:
        config = getYamlContext(file)
    if config == {}:
        config = {"MaxPrintBug": MAXINT}
        error("Cannot find the configuration, please check the RSCchecker-config.yml")
    MaxBug = config["MaxPrintBug"]
    MaxWarn = config["MaxPrintWarn"]
    ignores = config["ignores"]
    scan_files = config["scan-files"]
    addons = scan_files["addons"]
    if addons == ["example"]:
        warn("Only 'example' was selected. Did you forget to change it?")
    checkers = [
        # int just a placeholder
        int if ignores["ignoreGroups"] else checkGroups,
        int if ignores["ignoreRecipeTypes"] else checkRecipeTypes,
        int if ignores["ignoreMobDrops"] else checkMobDrops,
        int if ignores["ignoreGeoResources"] else checkGeoResources,
        int if ignores["ignoreItems"] else checkItems,
        int if ignores["ignoreArmors"] else checkArmors,
        int if ignores["ignoreCapacitors"] else checkCapacitors,
        int if ignores["ignoreFoods"] else checkFoods,
        int if ignores["ignoreMenus"] else checkMenus,
        int if ignores["ignoreGenerators"] else checkGenerators,
        int if ignores["ignoreSolarGenerators"] else checkSolarGenerators,
        int if ignores["ignoreMaterialGenerators"] else checkMaterialGenerators,
        int if ignores["ignoreMachines"] else checkMachines,
        int if ignores["ignoreRecipeMachines"] else checkRecipeMachines,
        int if ignores["ignoreSimpleMachines"] else checkSimpleMachines,
        int if ignores["ignoreMultiblockMachines"] else checkMultiblockMachines,
        int if ignores["ignoreSupers"] else checkSupers,
        int if ignores["ignoreTemplateMachines"] else checkTemplateMachines,
        int if ignores["ignoreResearches"] else checkResearches
    ]
    RewriteSlimefunItems()
    SlimefunItems = set(getSlimefunItems())
    LOADED_ITEMS = getVanillaItems()
    VANILLA_ITEMS = set((tuple(i.keys())[0] for i in LOADED_ITEMS))
    keys = []
    values = []
    for item in LOADED_ITEMS:
        keys.append(tuple(item.keys())[0])
        values.append(tuple(item.values())[0])
    MaxStacks = dict(zip(keys, values))
    entities = set()
    for item in VANILLA_ITEMS:
        if item[-10:] == "_SPAWN_EGG":
            entities.add(item[:-10])
    entities.add("GIANT")
    entities.add("MUSHROOM_COW")
    entities.remove("MOOSHROOM")
    checkAll()
    position = " "
except FileNotFoundError as err:
    error("Cannot find the file")
    error(err)
finally:
    info(f"{color.cyan}Done! {time() - sum_start}s")
    info(f"{color.cyan}Bug total: {totalBug}")
    info(f"{color.cyan}Warn total: {totalWarn}")
    info(f"{color.cyan}In fact, this simple script cannot find all the bugs ;)")
    info(f"Made by guguguhello")
    input("Press Enter to exit...")
