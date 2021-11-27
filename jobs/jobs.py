import sys
from jobs import getFullData, getTotalValue, addMonth, pop, count, wasted


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
		"func": getTotalValue.getTotalValue
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
	}
]

sys.modules[__name__] = jobs