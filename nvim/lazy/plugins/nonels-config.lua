return {
  "nvimtools/none-ls.nvim",

  opts = function(_, opts)
    local nls = require("null-ls")
    opts.sources = vim.list_extend(opts.sources or {}, {
      nls.builtins.formatting.fish_indent,
      nls.builtins.diagnostics.fish,
      nls.builtins.formatting.stylua,
      nls.builtins.formatting.shfmt,
      nls.builtins.formatting.csharpier,
      nls.builtins.formatting.black,
      nls.builtins.diagnostics.pylint.with({
        diagnostics_postprocess = function(diagnostic)
          diagnostic.code = diagnostic.message_id
        end,
      }),
      -- nls.builtins.diagnostics.ktlint,
      -- nls.builtins.formatting.ktlint,
    })
  end,
}
