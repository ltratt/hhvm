(*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the "hack" directory of this source tree.
 *
 *)

(** Conservatively determines if an expression can be captured. This is useful
    for deciding when to paranthesise an expression.

    For example,

        `identity(1 + 2) * 3` -> `1 + 2 * 3`

    would be wrong because binary operations can be captured, but

        `identity($foo->bar) * 3` -> `$foo->bar * 3`

    is not wrong and cannot be wrong in any context because `$foo->bar` cannot
    be captured.
*)
val can_be_captured : ('a, 'b) Aast_defs.expr_ -> bool

(** If the expression is an ExpressionTree with a "type" field in the shape that is the
    second argumentto MakeTree, that's the virtualized expression. Return it. Otherwise,
    return the input expression
*)
val get_virtual_expr : ('a, 'b) Aast_defs.expr -> ('a, 'b) Aast_defs.expr

(** If expression_tree has a"type" field in the shape that is the second
argumentto MakeTree, that's the virtualized expression. Return it. Otherwise,
return None
*)
val get_virtual_expr_from_et :
  ('a, 'b) Aast_defs.expression_tree -> ('a, 'b) Aast_defs.expr option
(** Get the leading assignments in an expression tree's lambda expression. *)

val get_splices_from_et :
  ('a, 'b) Aast_defs.expression_tree -> ('a, 'b) Aast_defs.stmt list

(** Gets the fun_ of a (possibly Hole wrapped) Efun or Lfun *)
val get_fun_expr : ('a, 'b) Aast_defs.expr -> ('a, 'b) Aast_defs.fun_ option

(** True iff the expression is definitely not going to have any side effects.
    This is a conservative syntactic check only, so calls always return false. *)
val is_const_expr : ('a, 'b) Aast_defs.expr -> bool
