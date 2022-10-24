require'lspconfig'.kotlin_language_server.setup{}
require'lspconfig'.pylsp.setup{}
require'lspconfig'.pyright.setup{}
require'lspconfig'.html.setup{}
require'lspconfig'.cssls.setup{}

-- lspconfig compatibilies
local capabilities = require('cmp_nvim_lsp').default_capabilities()
local lspconfig = require('lspconfig')

local csslsCompatibilities = vim.lsp.protocol.make_client_capabilities()
csslsCompatibilities.textDocument.completion.completionItem.snippetSupport = true

local servers = {'kotlin_language_server', 'pylsp', 'pyright', 'html', 'cssls'}
for _, lsp in ipairs(servers) do
    lspconfig[lsp].setup{
        capabilities = capabilities,
    }
end

local cmp = require 'cmp'
cmp.setup({
    snippet = {
        expand = function(args) 
            vim.fn["vsnip#anonymous"](args.body)
        end,
    },
    sources = ({
        { name = 'vsnip'},
        { name = 'buffer'},
        { name = 'nvim_lsp'}, 
        { name = 'path'},
        { name = 'cmdline'},
    }),
    mapping = cmp.mapping.preset.insert({
       ['<CR>'] = cmp.mapping.confirm {
            behavior = cmp.ConfirmBehavior.Replace,
            select = true,
        },
    }),
})
