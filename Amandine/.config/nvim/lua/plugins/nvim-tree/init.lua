require("nvim-tree").setup({
	hijack_cursor = true,
	open_on_setup = true,
	open_on_setup_file = true,
	open_on_tab = true,
	filters = {
		dotfiles = false,
	},
	view = {
		adaptive_size = true,
		number = true,
		signcolumn = "auto",
		mappings = {
			list = {
				{key = "t", action = "tabnew"},
				{key = "vs", action = "vsplit"},
				{key = "ss", action = "split"},
			}
		},
	},
	renderer = {
		highlight_git = true,
	},
	update_focused_file = {
		enable = true,
	},
	diagnostics = {
		enable = true,
	},
})
