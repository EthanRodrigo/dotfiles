vim.opt.termguicolors = true
require("bufferline").setup{
    options = {
        max_name_length = 15,
        color_icons = true,
        show_buffer_icons = true,
        show_buffer_default_icon = true,
        show_close_icon = true,
        show_tab_indicator = true,
        seperator_style = "padded_slant",
        numbers = "ordinal",
        diagnostic = "nvim_lsp",
        indicator = { style = 'underline' },
        offsets  = {
            {
                filetype = "NvimTree",
                text = "File Explorer",
                text_align = "center",
                seperator = true
            }
        }
    },
}

for i=1, 9 do 
    vim.api.nvim_set_keymap('n', 'b' .. tostring(i), ':BufferLineGoToBuffer ' .. tostring(i) .. '<CR>', {noremap})
end

vim.api.nvim_set_keymap('n', 'bn', ':BufferLineCycleNext<CR>', {noremap=true})
vim.api.nvim_set_keymap('n', 'bp', ':BufferLineCyclePrev<CR>', {noremap=true})
