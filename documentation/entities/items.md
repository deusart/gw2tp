# Items
## Fields:  
**id** (number) – The item id.  
**chat_link** (string) – The chat link.  
**name** (string) – The item name.  
**icon** (string, optional) – The full icon URL.  
**description** (string, optional) – The item description.  
**type** (string) – The item type (see below).  
**rarity** (string) – The item rarity.  
**level** (number) – The required level.  
**vendor_value** (number) – The value in coins when selling to a vendor. (Can be non-zero even when the item has the NoSell flag.)  
**default_skin** (number, optional) – The default skin id.  
**flags** (array of strings) – Flags applying to the item. Possible values:  
```
AccountBindOnUse – Account bound on use
AccountBound – Account bound on acquire
Attuned - If the item is Attuned
BulkConsume - If the item can be bulk consumed
DeleteWarning - If the item will prompt the player with a warning when deleting
HideSuffix – Hide the suffix of the upgrade component
Infused - If the item is infused
MonsterOnly
NoMysticForge – Not usable in the Mystic Forge
NoSalvage – Not salvageable
NoSell – Not sellable
NotUpgradeable – Not upgradeable
NoUnderwater – Not available underwater
SoulbindOnAcquire – Soulbound on acquire
SoulBindOnUse – Soulbound on use
Tonic - If the item is a tonic
Unique – Unique
```
**game_types** (array of strings) – The game types in which the item is usable. At least one game type is specified.  
**restrictions** (array of strings) – Restrictions applied to the item.  
**upgrades_into** (array, optional) – Lists what items this item can be upgraded into, and the method of upgrading.  
```
Each object in the array has the following attributes:
    upgrade (string) – Describes the method of upgrading.     
    Possible values:
        Attunement
        Infusion    
    item_id (integer) – The item ID that results from performing the upgrade.
```
**upgrades_from** (array, optional) – Lists what items this item can be upgraded from, and the method of upgrading. See upgrades_into for format.  
**details** (object, optional) – Additional item details if applicable, depending on the item type (see below).  

## Needed Fields
