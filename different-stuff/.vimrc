"(>^.^<)"
" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')
" Make sure you use single quotes

"YOU_COMPLETE_ME"
Plug 'https://github.com/ycm-core/YouCompleteMe'

"GRUV_BOX"
Plug 'https://github.com/morhetz/gruvbox'

"NERD_TREE"
Plug 'https://github.com/preservim/nerdtree'

" Initialize plugin system
call plug#end()

"!!!!!!!!!STUFF_FOR_PUGINS!!!!!!!!!"

let g:ycm_autoclose_preview_window_after_completion = 1

set background=dark
let g:gruvbox_contrast_dark = 'soft'
autocmd vimenter * ++nested colorscheme gruvbox

autocmd VimEnter * NERDTree | wincmd p
" Exit Vim if NERDTree is the only window left.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() |
    \ quit | endif
"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!HERE GOES MY PART!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
"Setting variables here"
:let mapleader = "-"
:let maplocalleader = "\\"

:set foldlevelstart=0
:set wrap number numberwidth=1

"-------Mappings for me <3-------"
"NORMAL_MODE_MAPPINGS --------------- {{{"
:nnoremap <leader>d dd
:nnoremap <localleader>u veU
:nnoremap <leader>ev :vsplit $MYVIMRC<cr>
:nnoremap <leader>sv :source $MYVIMRC<cr>
:nnoremap <leader>ss iSHIT<esc>l
:nnoremap H 0
:nnoremap L $
:nnoremap ++ :vertical resize +5<cr>
:nnoremap -- :vertical resize -5<cr>
" }}}

"python"
:nnoremap <localleader>cp :!python %<cr>

"INSERT_MODE"
:inoremap <localleader>u <esc>veUli
:inoremap jkjk <esc>

"Abbreviations go below" 
:iabbrev 1kir Kirish_Example@example.com
:iabbrev 1sig --<cr>Kirish<cr>Kirish_Example@example.com

"Terminal"
:set splitbelow
:term ++rows=20
:set splitbelow!

"----------AUTOCMDs----------"
:autocmd FileType python nnoremap <localleader>c I#<esc>

" Vimscript file settings ----------------- {{{
:augroup filetype_vim
:	autocmd!
:	autocmd FileType vim setlocal foldmethod=marker
:augroup END
" }}}

"----------STATUS_LINE----------"
" LINE_COUNTER --------------------- {{{
:set statusline=%F	"Full path to the file
:set statusline+=%=	"Switch to the right side
:set statusline+=%l	"Current line
:set statusline+=/	"Separator for current line
:set statusline+=%L	"Total lines
" }}}

