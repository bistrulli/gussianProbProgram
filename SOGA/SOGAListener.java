// Generated from SOGA.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SOGAParser}.
 */
public interface SOGAListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SOGAParser#progr}.
	 * @param ctx the parse tree
	 */
	void enterProgr(SOGAParser.ProgrContext ctx);
	/**
	 * Exit a parse tree produced by {@link SOGAParser#progr}.
	 * @param ctx the parse tree
	 */
	void exitProgr(SOGAParser.ProgrContext ctx);
	/**
	 * Enter a parse tree produced by {@link SOGAParser#instr}.
	 * @param ctx the parse tree
	 */
	void enterInstr(SOGAParser.InstrContext ctx);
	/**
	 * Exit a parse tree produced by {@link SOGAParser#instr}.
	 * @param ctx the parse tree
	 */
	void exitInstr(SOGAParser.InstrContext ctx);
	/**
	 * Enter a parse tree produced by {@link SOGAParser#ifclause}.
	 * @param ctx the parse tree
	 */
	void enterIfclause(SOGAParser.IfclauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SOGAParser#ifclause}.
	 * @param ctx the parse tree
	 */
	void exitIfclause(SOGAParser.IfclauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SOGAParser#elseclause}.
	 * @param ctx the parse tree
	 */
	void enterElseclause(SOGAParser.ElseclauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SOGAParser#elseclause}.
	 * @param ctx the parse tree
	 */
	void exitElseclause(SOGAParser.ElseclauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SOGAParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(SOGAParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link SOGAParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(SOGAParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link SOGAParser#lexpr}.
	 * @param ctx the parse tree
	 */
	void enterLexpr(SOGAParser.LexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link SOGAParser#lexpr}.
	 * @param ctx the parse tree
	 */
	void exitLexpr(SOGAParser.LexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link SOGAParser#bexpr}.
	 * @param ctx the parse tree
	 */
	void enterBexpr(SOGAParser.BexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link SOGAParser#bexpr}.
	 * @param ctx the parse tree
	 */
	void exitBexpr(SOGAParser.BexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link SOGAParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(SOGAParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link SOGAParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(SOGAParser.ExprContext ctx);
}