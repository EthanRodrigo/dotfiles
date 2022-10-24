" Core configs
lua require('core.mappings')
lua require('core.opts')

" Plugins
" Defined
lua require('plugins')
lua require('plugins.nvim-tree')
lua require('plugins.duskfox')
lua require('plugins.bufferline')
lua require('plugins.lualine')
lua require('plugins.blankline')
lua require('plugins.nvim-cmp')
lua require('plugins.treesitter')
lua require('plugins.telescope')

" Default
lua require('mason').setup()
lua require('colorizer').setup()

colorscheme duskfox
