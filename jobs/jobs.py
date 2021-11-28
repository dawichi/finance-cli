import sys
from jobs import getFullData, getCurrentValue, addMonth, pop, count, wasted, details


# ┌────────────────────────────────────────────────────────────
# │  Jobs index: functions available in the CLI
# └──────────────────────────────────────────────────────────── 
jobs = [
	{
		"name": "Full data",
		"func": getFullData.getFullData
	},
	{
		"name": "Total value",
		"func": getCurrentValue.getCurrentValue
	},
	{
		"name": "Add month",
		"func": addMonth.addMonth
	},
	{
		"name": "Count months logged",
		"func": count.count
	},
	{
		"name": "Delete last month",
		"func": pop.pop
	},
	{
		"name": "Wasted money by month",
		"func": wasted.wasted
	},
	{
		"name": "Details",
		"func": details.details
	}
]

sys.modules[__name__] = jobs