return {
  "stevearc/conform.nvim",
  require("conform").setup({
    formatters_by_ft = {
      cs = { "csharpier" },
      python = { "black" },
    },
  }),
}
