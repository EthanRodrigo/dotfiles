vim.cmd([[
  augroup packer_user_config
    autocmd!
    autocmd BufWritePost plugins.lua source <afile> | PackerCompile
  augroup end
]])

local ensure_packer = function()
  local fn = vim.fn
  local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
  if fn.empty(fn.glob(install_path)) > 0 then
    fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
    vim.cmd [[packadd packer.nvim]]
    return true
  end
  return false
end

local packer_bootstrap = ensure_packer()

return require('packer').startup(function(use)
	-- The Packer plugin
	use 'wbthomason/packer.nvim'

	-- nvim-tree
	use {
		'nvim-tree/nvim-tree.lua',
		requires = {
		'nvim-tree/nvim-web-devicons', -- optional, for file icons
		},
		tag = 'nightly' -- optional, updated every week. (see issue #1193)
	}

	-- the theme
	use "EdenEast/nightfox.nvim" 

	-- bufferline 
    use {
		'akinsho/bufferline.nvim', 
		tag = "v3.*", 
		requires = 'kyazdani42/nvim-web-devicons'
    }

    -- status line
    use {
        'nvim-lualine/lualine.nvim',
        requires = { 'kyazdani42/nvim-web-devicons', opt = true }
    }

    -- indent lines
    use "lukas-reineke/indent-blankline.nvim"

    -- autocompletion 
    use{
        'hrsh7th/nvim-cmp',
        requires = {
            {'neovim/nvim-lspconfig'},
            {'hrsh7th/cmp-nvim-lsp'},
            {'hrsh7th/cmp-buffer'},
            {'hrsh7th/cmp-path'},
            {'hrsh7th/cmp-cmdline'},
            {'hrsh7th/cmp-vsnip'},
        }
    }
    use { "williamboman/mason.nvim" }

    -- fuzzy file finder
    use {
        'nvim-telescope/telescope.nvim', tag = '0.1.0',
        requires = { {'nvim-lua/plenary.nvim'} }
    }
    use {'nvim-telescope/telescope-fzf-native.nvim', run = 'cmake -S. -Bbuild -DCMAKE_BUILD_TYPE=Release && cmake --build build --config Release && cmake --install build --prefix build' }

    -- syntax highlighting
    use {
        'nvim-treesitter/nvim-treesitter',
        run = ':TSUpdate',
    }

    -- startup 
    use {
        'goolord/alpha-nvim',
        config = function ()
            require'alpha'.setup(require'alpha.themes.dashboard'.config)
        end
    }
     
    -- colorizer 
    use{
        'norcalli/nvim-colorizer.lua'
    }

    -- git signs 
    use {
        'lewis6991/gitsigns.nvim',
        config = function()
            require('gitsigns').setup()
        end
    }


  	-- Automatically set up your configuration after cloning packer.nvim
  	-- Put this at the end after all plugins
	if packer_bootstrap then
  -- tag = 'release' -- To use the latest release (do not use this if you run Neovim nightly or dev builds!)
		require('packer').sync()
	end
end)
