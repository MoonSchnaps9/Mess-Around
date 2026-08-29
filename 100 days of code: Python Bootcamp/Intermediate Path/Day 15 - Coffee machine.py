# ============================================================
# DAY 15 — COFFEE MACHINE
# ============================================================
#
# ------------------------------------------------------------
# 1. PROMPT USER
# ------------------------------------------------------------
#    "What would you like? (espresso/latte/cappuccino): "
#    - Check the user's input to decide what to do next.
#    - The prompt should show every time an action has completed,
#      e.g. once the drink is dispensed, the prompt shows again
#      to serve the next customer.
#
# ------------------------------------------------------------
# 2. TURN OFF THE MACHINE
# ------------------------------------------------------------
#    - Entering "off" at the prompt is the maintainer's secret word.
#    - Code execution should end when this happens.
#
# ------------------------------------------------------------
# 3. PRINT REPORT
# ------------------------------------------------------------
#    - Entering "report" prints the current resource values, e.g.
#
#        Water: 100ml
#        Milk: 50ml
#        Coffee: 76g
#        Money: $2.5
#
# ------------------------------------------------------------
# 4. CHECK RESOURCES SUFFICIENT?
# ------------------------------------------------------------
#    - When a drink is chosen, check there are enough resources.
#    - E.g. Latte requires 200ml water but only 100ml is left:
#      do not make the drink, print "Sorry there is not enough water."
#    - Same applies to any depleted resource (milk, coffee).
#
# ------------------------------------------------------------
# 5. PROCESS COINS
# ------------------------------------------------------------
#    - If resources are sufficient, prompt the user to insert coins.
#
#      COIN VALUES:
#        quarters = $0.25
#        dimes    = $0.10
#        nickles  = $0.05
#        pennies  = $0.01
#
#    - Calculate the monetary value inserted, e.g.
#      1 quarter, 2 dimes, 1 nickel, 2 pennies
#      = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
#
# ------------------------------------------------------------
# 6. CHECK TRANSACTION SUCCESSFUL?
# ------------------------------------------------------------
#    - Check enough money was inserted for the selected drink.
#      E.g. Latte costs $2.50, only $0.52 inserted:
#      "Sorry that's not enough money. Money refunded."
#    - If enough: the cost of the drink is added to the machine
#      as profit, reflected next time "report" is triggered.
#    - If too much: offer change, e.g.
#      "Here is $2.45 dollars in change."
#      Change is rounded to 2 decimal places.
#
# ------------------------------------------------------------
# 7. MAKE COFFEE
# ------------------------------------------------------------
#    - If the transaction is successful and resources are enough,
#      deduct the drink's ingredients from the machine resources.
#
#      BEFORE buying a latte:        AFTER buying a latte:
#        Water: 300ml                  Water: 100ml
#        Milk: 200ml                   Milk: 50ml
#        Coffee: 100g                  Coffee: 76g
#        Money: $0                     Money: $2.5
#
#    - Once deducted, tell the user "Here is your latte. Enjoy!"
#      (matching their choice of drink).
#
# ============================================================