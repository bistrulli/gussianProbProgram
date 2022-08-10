// Generated from SOGA.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SOGAParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, ID=20, NUM=21, COMM=22, WS=23, DIGIT=24;
	public static final int
		RULE_progr = 0, RULE_instr = 1, RULE_assignment = 2, RULE_conditional = 3, 
		RULE_ifclause = 4, RULE_elseclause = 5, RULE_block = 6, RULE_merge = 7, 
		RULE_lexpr = 8, RULE_bexpr = 9, RULE_expr = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"progr", "instr", "assignment", "conditional", "ifclause", "elseclause", 
			"block", "merge", "lexpr", "bexpr", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'='", "'skip'", "'end if'", "'if'", "'{'", "'}'", "'else'", 
			"'merge'", "'norm'", "'*'", "'+'", "'-'", "'<'", "'<='", "'=='", "'>='", 
			"'>'", "'^2'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "ID", "NUM", "COMM", 
			"WS", "DIGIT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "SOGA.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SOGAParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgrContext extends ParserRuleContext {
		public List<InstrContext> instr() {
			return getRuleContexts(InstrContext.class);
		}
		public InstrContext instr(int i) {
			return getRuleContext(InstrContext.class,i);
		}
		public ProgrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_progr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).enterProgr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).exitProgr(this);
		}
	}

	public final ProgrContext progr() throws RecognitionException {
		ProgrContext _localctx = new ProgrContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_progr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__4) | (1L << T__8) | (1L << ID))) != 0)) {
				{
				{
				setState(22);
				instr();
				setState(23);
				match(T__0);
				}
				}
				setState(29);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InstrContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ConditionalContext conditional() {
			return getRuleContext(ConditionalContext.class,0);
		}
		public MergeContext merge() {
			return getRuleContext(MergeContext.class,0);
		}
		public InstrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).enterInstr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).exitInstr(this);
		}
	}

	public final InstrContext instr() throws RecognitionException {
		InstrContext _localctx = new InstrContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_instr);
		try {
			setState(33);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(30);
				assignment();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(31);
				conditional();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 3);
				{
				setState(32);
				merge();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SOGAParser.ID, 0); }
		public LexprContext lexpr() {
			return getRuleContext(LexprContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).exitAssignment(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_assignment);
		try {
			setState(42);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(35);
				match(ID);
				setState(36);
				match(T__1);
				setState(39);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
				case 1:
					{
					setState(37);
					lexpr(0);
					}
					break;
				case 2:
					{
					setState(38);
					expr(0);
					}
					break;
				}
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				match(T__2);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConditionalContext extends ParserRuleContext {
		public IfclauseContext ifclause() {
			return getRuleContext(IfclauseContext.class,0);
		}
		public ElseclauseContext elseclause() {
			return getRuleContext(ElseclauseContext.class,0);
		}
		public ConditionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).enterConditional(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).exitConditional(this);
		}
	}

	public final ConditionalContext conditional() throws RecognitionException {
		ConditionalContext _localctx = new ConditionalContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_conditional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			ifclause();
			setState(45);
			elseclause();
			setState(46);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfclauseContext extends ParserRuleContext {
		public BexprContext bexpr() {
			return getRuleContext(BexprContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public IfclauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifclause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).enterIfclause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).exitIfclause(this);
		}
	}

	public final IfclauseContext ifclause() throws RecognitionException {
		IfclauseContext _localctx = new IfclauseContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_ifclause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(T__4);
			setState(49);
			bexpr();
			setState(50);
			match(T__5);
			setState(51);
			block();
			setState(52);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElseclauseContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ElseclauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseclause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).enterElseclause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).exitElseclause(this);
		}
	}

	public final ElseclauseContext elseclause() throws RecognitionException {
		ElseclauseContext _localctx = new ElseclauseContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_elseclause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(T__7);
			setState(55);
			match(T__5);
			setState(56);
			block();
			setState(57);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public List<InstrContext> instr() {
			return getRuleContexts(InstrContext.class);
		}
		public InstrContext instr(int i) {
			return getRuleContext(InstrContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).exitBlock(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(59);
				instr();
				setState(60);
				match(T__0);
				}
				}
				setState(64); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__4) | (1L << T__8) | (1L << ID))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MergeContext extends ParserRuleContext {
		public MergeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_merge; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).enterMerge(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).exitMerge(this);
		}
	}

	public final MergeContext merge() throws RecognitionException {
		MergeContext _localctx = new MergeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_merge);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LexprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SOGAParser.ID, 0); }
		public TerminalNode NUM() { return getToken(SOGAParser.NUM, 0); }
		public List<LexprContext> lexpr() {
			return getRuleContexts(LexprContext.class);
		}
		public LexprContext lexpr(int i) {
			return getRuleContext(LexprContext.class,i);
		}
		public LexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lexpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).enterLexpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).exitLexpr(this);
		}
	}

	public final LexprContext lexpr() throws RecognitionException {
		return lexpr(0);
	}

	private LexprContext lexpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		LexprContext _localctx = new LexprContext(_ctx, _parentState);
		LexprContext _prevctx = _localctx;
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_lexpr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(69);
				match(T__9);
				}
				break;
			case 2:
				{
				setState(70);
				match(ID);
				}
				break;
			case 3:
				{
				setState(71);
				match(NUM);
				}
				break;
			case 4:
				{
				setState(72);
				match(NUM);
				setState(73);
				match(T__10);
				setState(74);
				lexpr(2);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(82);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new LexprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_lexpr);
					setState(77);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(78);
					_la = _input.LA(1);
					if ( !(_la==T__11 || _la==T__12) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(79);
					lexpr(2);
					}
					} 
				}
				setState(84);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class BexprContext extends ParserRuleContext {
		public LexprContext lexpr() {
			return getRuleContext(LexprContext.class,0);
		}
		public TerminalNode NUM() { return getToken(SOGAParser.NUM, 0); }
		public BexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bexpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).enterBexpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).exitBexpr(this);
		}
	}

	public final BexprContext bexpr() throws RecognitionException {
		BexprContext _localctx = new BexprContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_bexpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			lexpr(0);
			setState(86);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(87);
			match(NUM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public LexprContext lexpr() {
			return getRuleContext(LexprContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SOGAListener ) ((SOGAListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(90);
			lexpr(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(99);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(97);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(92);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(93);
						match(T__10);
						setState(94);
						expr(3);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(95);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(96);
						match(T__18);
						}
						break;
					}
					} 
				}
				setState(101);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 8:
			return lexpr_sempred((LexprContext)_localctx, predIndex);
		case 10:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean lexpr_sempred(LexprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		case 2:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0018g\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0005\u0000\u001a\b\u0000\n\u0000\f\u0000\u001d\t\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001\"\b\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u0002(\b\u0002\u0001\u0002\u0003\u0002"+
		"+\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0004\u0006?\b\u0006\u000b\u0006\f\u0006@\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b"+
		"L\b\b\u0001\b\u0001\b\u0001\b\u0005\bQ\b\b\n\b\f\bT\t\b\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0005\nb\b\n\n\n\f\ne\t\n\u0001\n\u0000\u0002\u0010\u0014\u000b"+
		"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0000\u0002\u0001"+
		"\u0000\f\r\u0001\u0000\u000e\u0012g\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0002!\u0001\u0000\u0000\u0000\u0004*\u0001\u0000\u0000\u0000\u0006,"+
		"\u0001\u0000\u0000\u0000\b0\u0001\u0000\u0000\u0000\n6\u0001\u0000\u0000"+
		"\u0000\f>\u0001\u0000\u0000\u0000\u000eB\u0001\u0000\u0000\u0000\u0010"+
		"K\u0001\u0000\u0000\u0000\u0012U\u0001\u0000\u0000\u0000\u0014Y\u0001"+
		"\u0000\u0000\u0000\u0016\u0017\u0003\u0002\u0001\u0000\u0017\u0018\u0005"+
		"\u0001\u0000\u0000\u0018\u001a\u0001\u0000\u0000\u0000\u0019\u0016\u0001"+
		"\u0000\u0000\u0000\u001a\u001d\u0001\u0000\u0000\u0000\u001b\u0019\u0001"+
		"\u0000\u0000\u0000\u001b\u001c\u0001\u0000\u0000\u0000\u001c\u0001\u0001"+
		"\u0000\u0000\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001e\"\u0003\u0004"+
		"\u0002\u0000\u001f\"\u0003\u0006\u0003\u0000 \"\u0003\u000e\u0007\u0000"+
		"!\u001e\u0001\u0000\u0000\u0000!\u001f\u0001\u0000\u0000\u0000! \u0001"+
		"\u0000\u0000\u0000\"\u0003\u0001\u0000\u0000\u0000#$\u0005\u0014\u0000"+
		"\u0000$\'\u0005\u0002\u0000\u0000%(\u0003\u0010\b\u0000&(\u0003\u0014"+
		"\n\u0000\'%\u0001\u0000\u0000\u0000\'&\u0001\u0000\u0000\u0000(+\u0001"+
		"\u0000\u0000\u0000)+\u0005\u0003\u0000\u0000*#\u0001\u0000\u0000\u0000"+
		"*)\u0001\u0000\u0000\u0000+\u0005\u0001\u0000\u0000\u0000,-\u0003\b\u0004"+
		"\u0000-.\u0003\n\u0005\u0000./\u0005\u0004\u0000\u0000/\u0007\u0001\u0000"+
		"\u0000\u000001\u0005\u0005\u0000\u000012\u0003\u0012\t\u000023\u0005\u0006"+
		"\u0000\u000034\u0003\f\u0006\u000045\u0005\u0007\u0000\u00005\t\u0001"+
		"\u0000\u0000\u000067\u0005\b\u0000\u000078\u0005\u0006\u0000\u000089\u0003"+
		"\f\u0006\u00009:\u0005\u0007\u0000\u0000:\u000b\u0001\u0000\u0000\u0000"+
		";<\u0003\u0002\u0001\u0000<=\u0005\u0001\u0000\u0000=?\u0001\u0000\u0000"+
		"\u0000>;\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@>\u0001\u0000"+
		"\u0000\u0000@A\u0001\u0000\u0000\u0000A\r\u0001\u0000\u0000\u0000BC\u0005"+
		"\t\u0000\u0000C\u000f\u0001\u0000\u0000\u0000DE\u0006\b\uffff\uffff\u0000"+
		"EL\u0005\n\u0000\u0000FL\u0005\u0014\u0000\u0000GL\u0005\u0015\u0000\u0000"+
		"HI\u0005\u0015\u0000\u0000IJ\u0005\u000b\u0000\u0000JL\u0003\u0010\b\u0002"+
		"KD\u0001\u0000\u0000\u0000KF\u0001\u0000\u0000\u0000KG\u0001\u0000\u0000"+
		"\u0000KH\u0001\u0000\u0000\u0000LR\u0001\u0000\u0000\u0000MN\n\u0001\u0000"+
		"\u0000NO\u0007\u0000\u0000\u0000OQ\u0003\u0010\b\u0002PM\u0001\u0000\u0000"+
		"\u0000QT\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000\u0000RS\u0001\u0000"+
		"\u0000\u0000S\u0011\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000\u0000"+
		"UV\u0003\u0010\b\u0000VW\u0007\u0001\u0000\u0000WX\u0005\u0015\u0000\u0000"+
		"X\u0013\u0001\u0000\u0000\u0000YZ\u0006\n\uffff\uffff\u0000Z[\u0003\u0010"+
		"\b\u0000[c\u0001\u0000\u0000\u0000\\]\n\u0002\u0000\u0000]^\u0005\u000b"+
		"\u0000\u0000^b\u0003\u0014\n\u0003_`\n\u0001\u0000\u0000`b\u0005\u0013"+
		"\u0000\u0000a\\\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000\u0000be\u0001"+
		"\u0000\u0000\u0000ca\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000"+
		"d\u0015\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000\t\u001b!\'*"+
		"@KRac";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}