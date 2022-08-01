// Generated from SOGA.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SOGALexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, ID=20, NUM=21, COMM=22, WS=23, DIGIT=24;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "ID", "NUM", "COMM", "WS", "ALPHA", "DIGIT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'='", "'end if'", "'skip'", "'merge'", "'if'", "'{'", "'}'", 
			"'else'", "'norm'", "'*'", "'+'", "'-'", "'<'", "'<='", "'=='", "'>='", 
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


	public SOGALexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "SOGA.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0018\u009c\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0005\u0013t\b\u0013\n\u0013\f\u0013w\t\u0013\u0001\u0014\u0004"+
		"\u0014z\b\u0014\u000b\u0014\f\u0014{\u0001\u0014\u0001\u0014\u0005\u0014"+
		"\u0080\b\u0014\n\u0014\f\u0014\u0083\t\u0014\u0003\u0014\u0085\b\u0014"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0005\u0015\u008b\b\u0015"+
		"\n\u0015\f\u0015\u008e\t\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u008c\u0000\u0019\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d"+
		"\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/"+
		"\u00001\u0018\u0001\u0000\u0003\u0003\u0000\t\n\r\r  \u0002\u0000AZaz"+
		"\u0001\u000009\u00a0\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000"+
		"\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000"+
		"\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000"+
		"\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000"+
		"\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000"+
		"%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u00001\u0001\u0000\u0000\u0000\u00013\u0001\u0000\u0000\u0000\u0003"+
		"5\u0001\u0000\u0000\u0000\u00057\u0001\u0000\u0000\u0000\u0007>\u0001"+
		"\u0000\u0000\u0000\tC\u0001\u0000\u0000\u0000\u000bI\u0001\u0000\u0000"+
		"\u0000\rL\u0001\u0000\u0000\u0000\u000fN\u0001\u0000\u0000\u0000\u0011"+
		"P\u0001\u0000\u0000\u0000\u0013U\u0001\u0000\u0000\u0000\u0015Z\u0001"+
		"\u0000\u0000\u0000\u0017\\\u0001\u0000\u0000\u0000\u0019^\u0001\u0000"+
		"\u0000\u0000\u001b`\u0001\u0000\u0000\u0000\u001db\u0001\u0000\u0000\u0000"+
		"\u001fe\u0001\u0000\u0000\u0000!h\u0001\u0000\u0000\u0000#k\u0001\u0000"+
		"\u0000\u0000%m\u0001\u0000\u0000\u0000\'p\u0001\u0000\u0000\u0000)y\u0001"+
		"\u0000\u0000\u0000+\u0086\u0001\u0000\u0000\u0000-\u0094\u0001\u0000\u0000"+
		"\u0000/\u0098\u0001\u0000\u0000\u00001\u009a\u0001\u0000\u0000\u00003"+
		"4\u0005;\u0000\u00004\u0002\u0001\u0000\u0000\u000056\u0005=\u0000\u0000"+
		"6\u0004\u0001\u0000\u0000\u000078\u0005e\u0000\u000089\u0005n\u0000\u0000"+
		"9:\u0005d\u0000\u0000:;\u0005 \u0000\u0000;<\u0005i\u0000\u0000<=\u0005"+
		"f\u0000\u0000=\u0006\u0001\u0000\u0000\u0000>?\u0005s\u0000\u0000?@\u0005"+
		"k\u0000\u0000@A\u0005i\u0000\u0000AB\u0005p\u0000\u0000B\b\u0001\u0000"+
		"\u0000\u0000CD\u0005m\u0000\u0000DE\u0005e\u0000\u0000EF\u0005r\u0000"+
		"\u0000FG\u0005g\u0000\u0000GH\u0005e\u0000\u0000H\n\u0001\u0000\u0000"+
		"\u0000IJ\u0005i\u0000\u0000JK\u0005f\u0000\u0000K\f\u0001\u0000\u0000"+
		"\u0000LM\u0005{\u0000\u0000M\u000e\u0001\u0000\u0000\u0000NO\u0005}\u0000"+
		"\u0000O\u0010\u0001\u0000\u0000\u0000PQ\u0005e\u0000\u0000QR\u0005l\u0000"+
		"\u0000RS\u0005s\u0000\u0000ST\u0005e\u0000\u0000T\u0012\u0001\u0000\u0000"+
		"\u0000UV\u0005n\u0000\u0000VW\u0005o\u0000\u0000WX\u0005r\u0000\u0000"+
		"XY\u0005m\u0000\u0000Y\u0014\u0001\u0000\u0000\u0000Z[\u0005*\u0000\u0000"+
		"[\u0016\u0001\u0000\u0000\u0000\\]\u0005+\u0000\u0000]\u0018\u0001\u0000"+
		"\u0000\u0000^_\u0005-\u0000\u0000_\u001a\u0001\u0000\u0000\u0000`a\u0005"+
		"<\u0000\u0000a\u001c\u0001\u0000\u0000\u0000bc\u0005<\u0000\u0000cd\u0005"+
		"=\u0000\u0000d\u001e\u0001\u0000\u0000\u0000ef\u0005=\u0000\u0000fg\u0005"+
		"=\u0000\u0000g \u0001\u0000\u0000\u0000hi\u0005>\u0000\u0000ij\u0005="+
		"\u0000\u0000j\"\u0001\u0000\u0000\u0000kl\u0005>\u0000\u0000l$\u0001\u0000"+
		"\u0000\u0000mn\u0005^\u0000\u0000no\u00052\u0000\u0000o&\u0001\u0000\u0000"+
		"\u0000pu\u0003/\u0017\u0000qt\u0003/\u0017\u0000rt\u00031\u0018\u0000"+
		"sq\u0001\u0000\u0000\u0000sr\u0001\u0000\u0000\u0000tw\u0001\u0000\u0000"+
		"\u0000us\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000v(\u0001\u0000"+
		"\u0000\u0000wu\u0001\u0000\u0000\u0000xz\u00031\u0018\u0000yx\u0001\u0000"+
		"\u0000\u0000z{\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000{|\u0001"+
		"\u0000\u0000\u0000|\u0084\u0001\u0000\u0000\u0000}\u0081\u0005.\u0000"+
		"\u0000~\u0080\u00031\u0018\u0000\u007f~\u0001\u0000\u0000\u0000\u0080"+
		"\u0083\u0001\u0000\u0000\u0000\u0081\u007f\u0001\u0000\u0000\u0000\u0081"+
		"\u0082\u0001\u0000\u0000\u0000\u0082\u0085\u0001\u0000\u0000\u0000\u0083"+
		"\u0081\u0001\u0000\u0000\u0000\u0084}\u0001\u0000\u0000\u0000\u0084\u0085"+
		"\u0001\u0000\u0000\u0000\u0085*\u0001\u0000\u0000\u0000\u0086\u0087\u0005"+
		"/\u0000\u0000\u0087\u0088\u0005*\u0000\u0000\u0088\u008c\u0001\u0000\u0000"+
		"\u0000\u0089\u008b\t\u0000\u0000\u0000\u008a\u0089\u0001\u0000\u0000\u0000"+
		"\u008b\u008e\u0001\u0000\u0000\u0000\u008c\u008d\u0001\u0000\u0000\u0000"+
		"\u008c\u008a\u0001\u0000\u0000\u0000\u008d\u008f\u0001\u0000\u0000\u0000"+
		"\u008e\u008c\u0001\u0000\u0000\u0000\u008f\u0090\u0005*\u0000\u0000\u0090"+
		"\u0091\u0005/\u0000\u0000\u0091\u0092\u0001\u0000\u0000\u0000\u0092\u0093"+
		"\u0006\u0015\u0000\u0000\u0093,\u0001\u0000\u0000\u0000\u0094\u0095\u0007"+
		"\u0000\u0000\u0000\u0095\u0096\u0001\u0000\u0000\u0000\u0096\u0097\u0006"+
		"\u0016\u0000\u0000\u0097.\u0001\u0000\u0000\u0000\u0098\u0099\u0007\u0001"+
		"\u0000\u0000\u00990\u0001\u0000\u0000\u0000\u009a\u009b\u0007\u0002\u0000"+
		"\u0000\u009b2\u0001\u0000\u0000\u0000\u0007\u0000su{\u0081\u0084\u008c"+
		"\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}