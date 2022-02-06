# Items
An item refers to any object which can physically appear in a character's inventory. The definition can be extended to bundles, objects the player can find in the environment and interact with but cannot keep. This is supported by consumable items that give bundles when used. This broad term therefore encompasses everything the player can carry, wield, wear, create or purchase. 

## Fields:  
**id** (number) – The item id.  
**chat_link** (string) – The chat link.  
**name** (string) – The item name.  
**icon** (string, optional) – The full icon URL.  
**description** (string, optional) – The item description.  
**type** (string) – The item type (see below). Possible values:  
- Armor – Armor
- Back – Back item
- Bag – Bags
- Consumable – Consumables
- Container – Containers
- CraftingMaterial – Crafting materials
- Gathering – Gathering tools
- Gizmo – Gizmos
- Key
- MiniPet – Miniatures
- Tool – Salvage kits
- Trait – Trait guides
- Trinket – Trinkets
- Trophy – Trophies
- UpgradeComponent – Upgrade components
- Weapon – Weapons

**rarity** (string) – The item rarity. Possible values:  
- Junk
- Basic
- Fine
- Masterwork
- Rare
- Exotic
- Ascended
- Legendary  

**level** (number) – The required level.  
**vendor_value** (number) – The value in coins when selling to a vendor. (Can be non-zero even when the item has the NoSell flag.)  
**default_skin** (number, optional) – The default skin id.  
**flags** (array of strings) – Flags applying to the item. Possible values:  
- AccountBindOnUse – Account bound on use
- AccountBound – Account bound on acquire
- Attuned - If the item is Attuned
- BulkConsume - If the item can be bulk consumed
- DeleteWarning - If the item will prompt the player with a warning when deleting
- HideSuffix – Hide the suffix of the upgrade component
- Infused - If the item is infused
- MonsterOnly
- NoMysticForge – Not usable in the Mystic Forge
- NoSalvage – Not salvageable
- NoSell – Not sellable
- NotUpgradeable – Not upgradeable
- NoUnderwater – Not available underwater
- SoulbindOnAcquire – Soulbound on acquire
- SoulBindOnUse – Soulbound on use
- Tonic - If the item is a tonic
- Unique – Unique  

**game_types** (array of strings) – The game types in which the item is usable. At least one game type is specified.  Possible values:
- Activity – Usable in activities
- Dungeon – Usable in dungeons
- Pve – Usable in general PvE
- Pvp – Usable in PvP
- PvpLobby – Usable in the Heart of the Mists
- Wvw – Usable in World vs. World  

**restrictions** (array of strings) – Restrictions applied to the item. Possible values:
- Activity – Usable in activities
- Dungeon – Usable in dungeons
- Pve – Usable in general PvE
- Pvp – Usable in PvP
- PvpLobby – Usable in the Heart of the Mists
- Wvw – Usable in World vs. World  

**upgrades_into** (array, optional) – Lists what items this item can be upgraded into, and the method of upgrading. Each object in the array has the following attributes:
- upgrade (string) – Describes the method of upgrading. Possible values:
    - Attunement
    - Infusion    
- item_id (integer) – The item ID that results from performing the upgrade.  

**upgrades_from** (array, optional) – Lists what items this item can be upgraded from, and the method of upgrading. See upgrades_into for format.  
**details** (object, optional) – Additional item details if applicable, depending on the item type (see below).  

## Needed Fields  
**id** (number)  
**name** (string)  
**type** (string)  
**rarity** (string)  
**level** (number)  
**vendor_value** (number)  
**flags** (array of strings)  
**game_types** (array of strings)  
**restrictions** (array of strings)  

## Web API Request example
**One Item equest (GET):**  
```
https://api.guildwars2.com/v2/items/12452
```
**List of Items (GET):**  
```
https://api.guildwars2.com/v2/items
```
**Response example**
```
{
  "name": "Omnomberry Bar",
  "type": "Consumable",
  "level": 80,
  "rarity": "Fine",
  "vendor_value": 33,
  "game_types": [
    "Wvw",
    "Dungeon",
    "Pve"
  ],
  "flags": [
    "NoSell"
  ],
  "restrictions": [],
  "id": 12452,
  "chat_link": "[&AgGkMAAA]",
  "icon": "https://render.guildwars2.com/file/6BD5B65FBC6ED450219EC86DD570E59F4DA3791F/433643.png",
  "details": {
    "type": "Food",
    "duration_ms": 1800000,
    "apply_count": 1,
    "name": "Nourishment",
    "icon": "https://render.guildwars2.com/file/779D3F0ABE5B46C09CFC57374DA8CC3A495F291C/436367.png",
    "description": "30% Magic Find\n40% Gold from Monsters\n+10% Experience from Kills"
  }
}
```