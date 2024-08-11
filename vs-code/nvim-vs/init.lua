local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  vim.fn.system({
    "git",
      "clone",
      "--filter=blob:none",
      "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup("plugins-nvim")

-- VSCode
local vscode = require("vscode")

-- Basic setup
vim.g.mapleader = " "
vim.cmd("set expandtab")
vim.cmd("set tabstop=2")
vim.cmd("set shiftwidth=2")
vim.cmd("set clipboard=unnamedplus")
vim.cmd("set relativenumber")
vim.cmd("set ignorecase")

-- Highlight yank
vim.api.nvim_create_autocmd("TextYankPost", {
  group = vim.api.nvim_create_augroup("highlight_yank", {}),
  desc = "Hightlight selection on yank",
  pattern = "*",
  callback = function()
    vim.highlight.on_yank { higroup = "IncSearch", timeout = 150 }
  end,
})

-- Windows
vim.keymap.set("n", "<leader>ww", "<C-W>p", { desc = "Other Window", remap = true })
vim.keymap.set("n", "<leader>wd", "<C-W>c", { desc = "Delete Window", remap = true })
vim.keymap.set("n", "<leader>w-", "<C-W>s", { desc = "Split Window Below", remap = true })
vim.keymap.set("n", "<leader>w|", "<C-W>v", { desc = "Split Window Right", remap = true })
vim.keymap.set("n", "<leader>-", "<C-W>s", { desc = "Split Window Below", remap = true })
vim.keymap.set("n", "<leader>|", "<C-W>v", { desc = "Split Window Right", remap = true })

-- Better tabulation/identation
vim.keymap.set("v", "<", "<gv")
vim.keymap.set("v", ">", ">gv")

-- Buffers
vim.keymap.set("n", "<leader>bd", function()
  vscode.action("workbench.action.closeActiveEditor")
end)
vim.keymap.set("n", "<S-h>", function()
  vscode.action("workbench.action.previousEditor")
end)
vim.keymap.set("n", "<S-l>", function()
  vscode.action("workbench.action.nextEditor")
end)

-- Code
vim.keymap.set("n", "<leader>ca", function()
  vscode.action("editor.action.sourceAction")
end)
vim.keymap.set("n", "<leader>cf", function()
  vscode.action("editor.action.formatDocument")
end)
vim.keymap.set("n", "gd", function()
  vscode.action("editor.action.revealDefinition")
end)
vim.keymap.set("n", "gi", function()
  vscode.action("editor.action.goToImplementation")
end)
vim.keymap.set("n", "gr", function()
  vscode.action("editor.action.goToReferences")
end)
vim.keymap.set("n", "[d", function()
  vscode.action("editor.action.marker.prev")
end)
vim.keymap.set("n", "]d", function()
  vscode.action("editor.action.marker.next")
end)

-- Move to window using the <ctrl> hjkl keys
vim.keymap.set("n", "<C-h>", "<C-w>h", { desc = "Go to Left Window", remap = true })
vim.keymap.set("n", "<C-j>", "<C-w>j", { desc = "Go to Lower Window", remap = true })
vim.keymap.set("n", "<C-k>", "<C-w>k", { desc = "Go to Upper Window", remap = true })
vim.keymap.set("n", "<C-l>", "<C-w>l", { desc = "Go to Right Window", remap = true })

-- Find
vim.keymap.set("n", "<leader>ff", function()
  vscode.action("workbench.action.quickOpen")
end)
vim.keymap.set("n", "<leader>fb", function()
  vscode.action("workbench.action.showAllEditors")
end)
vim.keymap.set("n", "<leader>fg", function()
  vscode.action("search.action.openNewEditor")
end)

-- Extras
vim.keymap.set("n", "<leader>gt", function()
  vscode.action("workbench.action.terminal.toggleTerminal")
end)
vim.keymap.set("n", "<leader>e", function()
  vscode.action("workbench.action.toggleSidebarVisibility")
end)
vim.keymap.set("n", "<leader>z", function()
  vscode.action("workbench.action.toggleZenMode")
end)

