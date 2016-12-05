# XV5 gui init module
# (c) 2001 Juergen Riegel LGPL

class XV5Workbench ( Workbench ):
	"XV5 workbench object"
	MenuText = "XV5"
	ToolTip = "XV5 workbench"
	def Initialize(self):
		# load the module
		import XV5Gui
	def GetClassName(self):
		return "XV5Gui::Workbench"

Gui.addWorkbench(XV5Workbench())
