try:
  emojis = input("Do you want to add emojis? (Y/N) ").lower()

  emerald_avg = int(input("Enter the emerald average: "))
  lapis_avg = int(input("Enter the lapis average: "))
  token_avg = int(input("Enter the token average: "))

  if emojis == 'y':
    print(":MysteryPickaxe: Mystery Pickaxe: $" + "{:,}".format(emerald_avg*12000))
    print(":RadioactivePickaxe: Radioactive Pickaxe: $" + "{:,}".format(emerald_avg * 7500))
    print(":RainbowPickaxe: Rainbow Pickaxe & :MidasSword: Midas Sword: $" + "{:,}".format(emerald_avg * 5000))
    print(":Trident: Trident: $" + "{:,}".format(emerald_avg * 7000))
    print(":Enchant: Tier 1 Enchantments: $" + "{:,}".format(lapis_avg * 100))
    print(":Dragon_Slayer: Dragon Slayer: $" + "{:,}".format(lapis_avg * 500))
    print(":Enchant: Efficiency: $" + "{:,}".format(lapis_avg * 750))
    print(":T5BoosterPickaxe: T5 Booster Pickaxe: $" + "{:,}".format(token_avg * 500))
    print(":T5boostersword: T5 Booster Sword & :t5boosteraxe: T5 Booster Axe: $" + "{:,}".format(token_avg * 400))
  else:
    print("Mystery Pickaxe: $" + "{:,}".format(emerald_avg*12000))
    print("Radioactive Pickaxe: $" + "{:,}".format(emerald_avg * 7500))
    print("Rainbow Pickaxe & Midas Sword: $" + "{:,}".format(emerald_avg * 5000))
    print("Trident: $" + "{:,}".format(emerald_avg * 7000))
    print("Tier 1 Enchantments: $" + "{:,}".format(lapis_avg * 100))
    print("Dragon Slayer: $" + "{:,}".format(lapis_avg * 500))
    print("Efficiency: $" + "{:,}".format(lapis_avg * 750))
    print("T5 Booster Pickaxe: $" + "{:,}".format(token_avg * 500))
    print("T5 Booster Sword & T5 Booster Axe: $" + "{:,}".format(token_avg * 400))

except ValueError:
  print("Enter a number (no commas).")
except:
  print("An error occured.")
