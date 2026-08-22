# Final Exercise — Space Station Resource Manager
#
# Build a resource management system for a space station.
#
# Data structure to start with:
# - A dictionary of crew members, each with a name, role, and status
# - A dictionary of resources with current stock levels
# - A log (list) of all transactions
#
# Functions required (each must return a value):
#   1. display_status(crew, resources) — prints crew and resource overview
#   2. add_resource(resources, item, quantity) — adds stock, logs the transaction
#   3. consume_resource(resources, log, item, quantity) — removes stock if available,
#      warns if not enough, logs the transaction
#   4. add_crew(crew, name, role) — adds a new crew member as "Active"
#   5. update_crew_status(crew, name, status) — updates a crew member's status
#      ("Active", "On EVA", "Injured", "Off Duty")
#   6. mission_report(crew, resources, log) — prints a full summary:
#      active crew count, critical resources (stock below 5), and last 3 log entries
#
# Requirements:
#   - All input handled via function parameters, not input() inside functions
#   - found = False pattern where needed
#   - Handle all edge cases: item not found, crew member not found,
#     invalid status, insufficient stock
#   - Call every function at least twice with different arguments to prove it works

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

