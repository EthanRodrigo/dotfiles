" General settings ---------------------------------------------------- {{{
set nu
set autoindent 
set tabstop=4 " tabsizes 
set shiftwidth=4
set laststatus=2
set nocompatible  " Disable compatibility with vi
set hlsearch " Highlighting on search
set foldmethod=marker " Folding with markers
filetype on " Detect the type of the file in use
filetype plugin on " Enable plugins and load them for detected filetype
filetype indent on " Enable indentation according to the filetype
" }}}

" Plugins -------------------------------------------------------------{{{
call plug#begin()
Plug 'ap/vim-css-color'
Plug 'vifm/vifm.vim'
Plug 'itchyny/lightline.vim'
Plug 'yuezk/vim-js'
Plug 'kyoz/purify', { 'rtp': 'vim' }
Plug 'vim-python/python-syntax'
call plug#end()
" }}}

" General settings ----------------------------------------------------- {{{
syntax on
colorscheme purify

" lightline settings
let g:lightline = {
	\'colorscheme': 'purify'
	\}

" python-syntax settings
let g:python_highlight_all = 1
" }}}

" Mapping ------------------------------------------------------------- {{{
" spacebar for : key
nnoremap <space> :

" Run, compile programs --------------------------------------------- {{{
" Python
nnoremap <f5>p :w <CR>:!python3 % <CR> 

" C
nnoremap <f5>c :w<CR>:!gcc -Wall -Wextra % -o '%:r' <CR>
nnoremap <f5>cr :!./'%:r' <CR>

" Cpp
nnoremap <f5>C :w<CR>:!g++ -Wall -Wextra % -o '%:r' <CR>
nnoremap <f5>Cr :!./'%:r' <CR>

" JS
nnoremap <F5>s :w<CR>:!node % <CR>
" }}}

" }}}
