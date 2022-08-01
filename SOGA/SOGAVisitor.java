// Generated from SOGA.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link SOGAParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface SOGAVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link SOGAParser#progr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgr(SOGAParser.ProgrContext ctx);
	/**
	 * Visit a parse tree produced by {@link SOGAParser#instr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInstr(SOGAParser.InstrContext ctx);
	/**
	 * Visit a parse tree produced by {@link SOGAParser#ifclause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfclause(SOGAParser.IfclauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SOGAParser#elseclause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElseclause(SOGAParser.ElseclauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SOGAParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(SOGAParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link SOGAParser#lexpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLexpr(SOGAParser.LexprContext ctx);
	/**
	 * Visit a parse tree produced by {@link SOGAParser#bexpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBexpr(SOGAParser.BexprContext ctx);
	/**
	 * Visit a parse tree produced by {@link SOGAParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(SOGAParser.ExprContext ctx);
}