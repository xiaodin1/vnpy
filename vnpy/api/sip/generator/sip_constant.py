LEN_ID = 32
LEN_SYS_ID = 40
LEN_SYMBOL = 32
LEN_SYMBOL_NAME = 64
LEN_ERR_MSG = 256
LEN_IP_ADDR = 40
LEN_CUST_ID = 19
LEN_PASSWORD = 65
LEN_ACCOUNT_ID = 33
LEN_CIF_TYPE = 3
LEN_TERM_INFO = 257
LEN_SECU_ID = 21
LEN_STK_CODE = 21
LEN_MONY_TYPE = 4
LEN_ORG_ID = 5
LEN_SEAT = 17
LEN_TA_CODE = 13
LEN_REMARK = 513
LEN_REMARK1 = 129
LEN_MARKET = 8
LogLevel_Debug = 1
LogLevel_Info = 0
LogLevel_Warn = 1
LogLevel_Error = 2
LogLevel_Critical = 3
SUCCESS = 0
ERR_HFT_TRADER_INTERNAL = 14000
ERR_HFT_TRADER_INVALID_PARAM = 14001
ERR_HFT_TRADER_NETWORK_TIMEOUT = 14002
ERR_HFT_TRADER_NETWORK_SEND_FAIL = 14003
ERR_HFT_TRADER_INVALID_PKG = 14004
ERR_HFT_TRADER_PACK_FAIL = 14005
ERR_HFT_TRADER_UNPACK_FAIL = 14006
ERR_HFT_TRADER_NO_MEM = 14007
ERR_HFT_TRADER_INIT_ERROR = 14008
ERR_HFT_TRADER_NOT_CONNECT = 14009
ERR_HFT_TRADER_LOGIN_FAIL = 14010
ERR_HFT_TRADER_NOT_INIT = 14011
ERR_HFT_TRADER_GW_ROUTE_FAIL = 14012
ERR_HFT_TRADER_GW_LOGIC_FAIL = 14013
ERR_HFT_TRADER_GW_KEYFIELD_FAIL = 14014
ERR_HFT_TRADER_GW_DECODE_FAIL = 14015
ERR_HFT_TRADER_GW_NO_USER = 14016
ERR_HFT_TRADER_GW_NO_COUNTERID = 14017
ERR_HFT_TRADER_GW_ERROR_IP = 14018
ERR_HFT_TRADER_GW_ERROR_MAC = 14019
ERR_HFT_TRADER_NO_DATA = 14020
ERR_HFT_TRADER_NO_CERT_FILE = 14021
ERR_HFT_TRADER_GW_UNKOWN_MSG = 14022
ERR_HFT_TRADER_GW_OVERRUN = 14023
ERR_HFT_TRADER_GW_FUNDID_DISABLE = 14024
ERR_HFT_TRADER_GW_INVALID_CID = 14025
ERR_HFT_TRADER_GW_USED_CID = 14026
ERR_HFT_TRADER_EXCEED_MAX_NUM = 14027
ERR_HFT_TRADER_SEQNO_NOT_UNIQUE = 14028
ERR_HFT_TRADER_GW_REQUIRE_MIN_API_VERSION = 14029
ERR_HFT_TRADER_UNSUPPORTED_FUNC = 14030
ERR_HFT_TRADER_BUFFER_OVERFLOW = 14031
ERR_HFT_TRADER_NOT_FOUND_SECUID = 14032
ERR_HFT_TRADER_CALL_MICRO_SERVICE = 14033
ERR_HFT_TRADER_MICRO_SERVICE_BIZERROR = 14034
Market_SSE = 1
Market_SZSE = 2
Market_SSE_OP = 10
Market_SZSE_OP = 11
OrderStatus_PendingNew = 1
OrderStatus_New = 2
OrderStatus_PartiallyFilled = 3
OrderStatus_Filled = 4
OrderStatus_PendingCancel = 5
OrderStatus_Canceling = 6
OrderStatus_CancelFilled = 7
OrderStatus_PartiallyCanceled = 8
OrderStatus_Rejected = 9
OrderStatus_CancelRejected = 10
OrderType_LMT = 1
OrderType_BOC = 2
OrderType_BOP = 3
OrderType_B5TC = 4
OrderType_B5TL = 5
OrderType_IOC = 6
OrderType_AON = 7
OrderType_ALMT = 9
OrderType_ELMT = 10
OrderType_OLMT = 11
OrderSide_Bid = 1
OrderSide_Ask = 2
OrderSide_Buy_Open = 3
OrderSide_Buy_Close = 4
OrderSide_Sell_Open = 5
OrderSide_Sell_Close = 6
OrderSide_Margin_Bid = 13
OrderSide_Margin_Ask = 14
OrderSide_Covered_Open = 15
OrderSide_Covered_Close = 16
OrderSide_ETF_Create = 17
OrderSide_ETF_Redeem = 18
OrderSide_Reverse_Repurchase = 19
OrderSide_Margin_EnBuyBack = 20
OrderSide_Margin_EnSellBack = 21
OrderSide_Margin_StockBack = 22
OrderSide_Margin_PayBack = 23
OrderSide_Margin_MortgageIn = 24
OrderSide_Margin_MortgageOut = 25
OrderSide_Repurchase = 26
OrderSide_IPO_Bid = 27
OrderSide_AHFPT_Bid = 28
OrderSide_AHFPT_Ask = 29
OrderSide_Margin_MoreStockTrans = 30
OrderSide_Allotment_Shares = 31
OrderSide_ETF_Create_OTC = 33
OrderSide_ETF_Redeem_OTC = 34
OrderSide_Bond_Swap = 35
OrderSide_Bond_Sell_Back = 36
OrderSide_Pledge_In = 37
OrderSide_Pledge_Out = 38
PositionSide_Long = 1
PositionSide_Short = 2
PositionSide_Short_Covered = 3
TradeReportType_Normal = 1
TradeReportType_Cancel = 2
TradeReportType_Abolish = 3
TradeReportType_InsideCancel = 4
TradeReportType_CancelAbolish = 5
AccountType_Stock = 1
AccountType_Futures = 2
AccountType_Options = 3
AccountType_Margin = 4
CurrencyType_CNY = 1
CurrencyType_HKD = 2
CurrencyType_USD = 3
CurrencyType_EUR = 4
CurrencyType_JPY = 5
CurrencyType_KRW = 6
CancelFlag_False = 1
CancelFlag_True = 2
ETFTradeState_PurchaseAndRedeem = 1
ETFTradeState_Forbidden = 2
ETFTradeState_OnlyPurchase = 3
ETFTradeState_OnlyRedeem = 4
ETFRepalceFlag_Forbidden = 1
ETFRepalceFlag_Allow = 2
ETFRepalceFlag_Must = 3
ETFRepalceFlag_NotSHRefund = 4
ETFRepalceFlag_NotSHMust = 5
ETFRepalceFlag_NotSHSZRefund = 6
ETFRepalceFlag_NotSHSZMust = 7
StkType_Stock = 1
StkType_Bond = 2
StkType_Index = 3
StkType_Future = 4
StkType_Options = 5
StkType_Fund = 6
StkType_Repurchase = 7
StkType_Warrant = 8
StkType_STIB = 9
SecurityTypeDetail_Default = 0
SecurityTypeDetail_ZBAG = 1
SecurityTypeDetail_ZXBG = 2
SecurityTypeDetail_CYBG = 3
SecurityTypeDetail_ZBBG = 4
SecurityTypeDetail_GZ = 5
SecurityTypeDetail_QYZ = 6
SecurityTypeDetail_GSZ = 7
SecurityTypeDetail_KZZ = 8
SecurityTypeDetail_SMZ = 9
SecurityTypeDetail_KJHSMZ = 10
SecurityTypeDetail_ZQGSCJZ = 11
SecurityTypeDetail_ZYSHG = 12
SecurityTypeDetail_ZCZCZQ = 13
SecurityTypeDetail_GPETF = 14
SecurityTypeDetail_KSCGPETF = 15
SecurityTypeDetail_KJETF = 16
SecurityTypeDetail_SWZQETF = 17
SecurityTypeDetail_XJZQETF = 18
SecurityTypeDetail_HJETF = 19
SecurityTypeDetail_HBETF = 20
SecurityTypeDetail_GGETF = 21
SecurityTypeDetail_SPQHETF = 22
SecurityTypeDetail_BZLOF = 23
SecurityTypeDetail_FJZJJ = 24
SecurityTypeDetail_FBSJJ = 25
SecurityTypeDetail_JSSJJ = 26
SecurityTypeDetail_PSQZ = 27
SecurityTypeDetail_QZ = 28
SecurityTypeDetail_GGQQ = 29
SecurityTypeDetail_ETFQQ = 30
SecurityTypeDetail_ZGCP = 31
SecurityTypeDetail_BJHG = 32
SecurityTypeDetail_YXG = 33
SecurityTypeDetail_ZQGSDQZ = 34
SecurityTypeDetail_KJHGSZ = 35
SecurityTypeDetail_ZQFX = 36
SecurityTypeDetail_GZFX = 37
SecurityTypeDetail_QTZQ = 38
SecurityTypeDetail_KSC = 39
SecurityTypeDetail_QTJJ = 40
SecurityTypeDetail_GJBGP = 41
SecurityTypeDetail_QTGP = 42
SecurityTypeDetail_MDSZQHG = 43
SecurityTypeDetail_CYBKZZ = 44
SecurityTypeDetail_CTPZ = 45
SecurityTypeDetail_HLTCDR = 46
SecurityTypeDetail_CXQYGP = 47
SecurityTypeDetail_ZYDM = 48
SecurityTypeDetail_SSSSHBJJ = 49
SecurityTypeDetail_XGXZFX = 50
SecurityTypeDetail_KCB = 51
SecurityTypeDetail_KCBCDR = 53
SecurityStatus_Normal = 0
SecurityStatus_Suspend = 1
SecurityStatus_NearExpireDate = 2
SecurityStatus_Adjustment = 3
SecurityStatus_ExcludeRight = 4
SecurityStatus_ExcludeDividend = 5
SecurityStatus_Caution = 6
SecurityStatus_IPOFirstDay = 7
SecurityStatus_Delisting = 8
SecurityStatus_TransferByAgreement = 9
CounterType_JZJY = 1
CounterType_APEX_MARGIN = 2
CounterType_APEX = 3
CounterType_DYC = 5
CounterType_DYC_MARGIN = 6
CounterType_DYC_JZJY = 8
CounterType_DYC_JZJY_MARGIN = 9
SecuidRight_Delisting = 1
SecuidRight_Caution = 2
SecuidRight_Gem = 3
SecuidRight_KeChuangPlate_Normal = 4
SecuidRight_KeChuangPlate_Credit = 5
SecuidRight_Repo = 6
SecuidRight_Reverse_Repo = 7
SecuidRight_SHHK_Trade = 8
SecuidRight_SZHK_Trade = 9
SecuidRight_ETF_Redemption_Normal = 10
SecuidRight_Hulun_Trade = 11
TransferFundSide_In = 1
TransferFundSide_Out = 2
OrderFlag_Security_Normal = 1
OrderFlag_Security_CashLoan = 2
OrderFlag_Security_SecurityLoan = 3
OrderFlag_Future_Option_Speculation = 4
OrderFlag_Future_Option_Hedge = 5
OrderFlag_Future_Option_Arbitrage = 6
OrderFlag_Option_Covered = 7
OrderQueryFlag_All = 0
OrderQueryFlag_Cancelable = 1
OrderQueryFlag_NonCancel = 2
IPOQueryFlag_NewStock = 1
IPOQueryFlag_NewBond = 2
ExerciseType_Execute = 1
ExerciseOperateStatus_InsertSubmitted = 1
ExerciseOperateStatus_CancelSubmitted = 2
ExerciseOperateStatus_Accepted = 3
ExerciseOperateStatus_InsertRejected = 4
ExerciseOperateStatus_CancelRejected = 5
ExerciseOperateStatus_UnSubmitted = 6
ExerciseStatus_SendStock = 1
ExerciseStatus_RepealStock = 2
ExerciseStatus_SendOffer = 3
ExerciseStatus_Fail = 4
ExerciseStatus_Accepted = 5
ExerciseStatus_Cancelled = 6
StrikeModeType_Continental = 1
StrikeModeType_American = 2
StrikeModeType_Bermuda = 3
OptionsType_CallOptions = 1
OptionsType_PutOptions = 2
OrderUnitType_Shou = 1
OrderUnitType_Gu = 2
OrderUnitType_Fen = 3
OrderUnitType_Zhang = 4
TransferStatus_TransferHandling = 1
TransferStatus_TransferSuccess = 2
TransferStatus_TransferFail = 3
TransferPositionType_All = 1
TransferPositionType_History = 2
TransferPositionType_TodayBS = 3
TransferPositionType_TodayPR = 4
TransferStockPositionSide_In = 1
TransferStockPositionSide_Out = 2
TransferStockPositionSide_MoveIn = 3
TransferStockPositionSide_MoveOut = 4
TransferStockPositionSide_Lock = 5
TransferStockPositionSide_Unlock = 6
TransferStockPositionSide_ExerciseFreeze = 7
TransferStockPositionSide_ExerciseUnfreeze = 8
TransferStockPositionSide_CoveredCloseUnfreeze = 9
LockStockType_Lock = 1
LockStockType_Unlock = 2
LockStockStatus_SendStock = 1
LockStockStatus_RepealStock = 2
LockStockStatus_SendOffer = 3
LockStockStatus_Fail = 4
LockStockStatus_Success = 5
LockStockStatus_ForceCancel = 6
ContractStatus_Suspend = 0x00000001
ContractStatus_LongTermSuspend = 0x00000002
ContractStatus_CircuitBreaker = 0x00000040
ContractStatus_RestrictLongOpen = 0x00000080
ContractStatus_RestrictShortOpen = 0x00000100
ContractStatus_RestrictCoveredOpen = 0x00000200
ContractStatus_VolatilityInterrupt = 0x00000400
ContractStatus_TempSuspend = 0x00000800
ContractStatus_ContinuousSuspend = 0x00001000
ContractStatus_RestrictExercise = 0x00002000
ContractStatus_RestrictMakerQuote = 0x00004000
OptionCombineType_Combine = 1
OptionCombineType_Split = 2
OptionCombineType_ForceSplit = 3
OptionCombineStrategy_CNSJC = 1
OptionCombineStrategy_CXSJC = 2
OptionCombineStrategy_PXSJC = 3
OptionCombineStrategy_PNSJC = 4
OptionCombineStrategy_KS = 5
OptionCombineStrategy_KKS = 6
OptionCombineStrategy_ZBD = 7
ApprovalStatus_NoCheck = 1
ApprovalStatus_CheckSucc = 2
ApprovalStatus_CheckFail = 3
ApprovalStatus_Expired = 4
ApprovalStatus_Cancelled = 5
ApprovalStatus_Extended = 6
MARKET_SH = "SH"
MARKET_SZ = "SZ"
MARKET_CFFEX = "CFFEX"
MARKET_CZCE = "CZCE"
MARKET_DCE = "DCE"
MARKET_SHFE = "SHFE"
MARKET_HK = "HK"
MARKET_SGE = "SGE"
MARKET_CFETS = "CFETS"
MARKET_SHOP = "SHOP"
MARKET_SZOP = "SZOP"
MARKET_SZHK = "SZHK"
MARKET_SHHK = "SHHK"
