local M = {}

function M.map(mode, lhs, rhs, opts)
    local options = { noremap = true}
    if opts then
        options = vim.tbl_extend("force", options, opts)
    end
    vim.api.nvim_set_keymap(mode, lhs, rhs, options)
end

-- The colon
M.map('n', '<space>', ':')

-- Exit 
M.map('n', '<F2>', ':w<CR>')
M.map('n', '<F3>', ':wq<CR>')
M.map('n', '<F4>', ':q<CR>')
M.map('n', '<F5>', ':q!<CR>')

-- Windows (Not Microsoft)
M.map('n', 'SS', ':new')
M.map('n', 'VS', ':vert new')

-- Run programs
-- Python
M.map('n', '<F6>p', ':!python3 %<CR>')

-- C
M.map('n', '<F6>c', ":w<CR>:!gcc -Wall -Wextra % -o '%:r' <CR>")
M.map('n', '<F6>cr', ":!./'%:r' <CR>")

-- Cpp
M.map('n', '<F6>cp', ":w<CR>:!g++ -Wall -Wextra % -o '%:r' <CR>")
M.map('n', '<F6>cpr', ":!./'%:r' <CR>")

-- JS
M.map('n', '<F6>js', ':w<CR>:!node % <CR>')

-- Plugins 
-- NvimTree
M.map('n', 'FF', ':NvimTreeFindFile<CR>') -- I just want this only
M.map('n', 'Fc', ':NvimTreeClose<CR>') -- I just want this only

return M
