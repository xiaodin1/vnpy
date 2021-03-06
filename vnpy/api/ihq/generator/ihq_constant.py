ISTONE_VERSION_LEN = 16
ISTONE_USERID_LEN = 16
ISTONE_USER_PW_LEN = 32
ISTONE_TRADING_DAY_LEN = 9
ISTONE_TIMESTAMP_LEN = 9
ISTONE_EXCHANGE_LEN = 16
ISTONE_TICKER_LEN = 16
ISTONE_TICKER_NAME_LEN = 64
ISTONE_LOCAL_ORDER_LEN = 11
ISTONE_ORDER_EXCH_LEN = 17
ISTONE_EXEC_ID_LEN = 18
ISTONE_BRANCH_PBU_LEN = 7
ISTONE_USERS_EXTERNAL = 1
ISTONE_USERS_OPERATOER = 2
ISTONE_USERS_AUDITOR = 3
ISTONE_LOG_LEVEL_FATAL = 0
ISTONE_LOG_LEVEL_ERROR = 1
ISTONE_LOG_LEVEL_WARNING = 2
ISTONE_LOG_LEVEL_INFO = 3
ISTONE_LOG_LEVEL_DEBUG = 4
ISTONE_LOG_LEVEL_TRACE = 5
ISTONE_PROTOCOL_TCP = 1
ISTONE_PROTOCOL_UDP = 2
ISTONE_EXCHANGE_SH = 1
ISTONE_EXCHANGE_SZ = 2
ISTONE_EXCHANGE_UNKNOWN = 3
ISTONE_MKT_INIT = 0
ISTONE_MKT_SZ_A = 1
ISTONE_MKT_SH_A = 2
ISTONE_MKT_UNKNOWN = 3
ISTONE_PRICE_LIMIT = 1
ISTONE_PRICE_BEST_OR_CANCEL = 2
ISTONE_PRICE_BEST5_OR_LIMIT = 3
ISTONE_PRICE_BEST5_OR_CANCEL = 4
ISTONE_PRICE_ALL_OR_CANCEL = 5
ISTONE_PRICE_FORWARD_BEST = 6
ISTONE_PRICE_REVERSE_BEST_LIMIT = 7
ISTONE_PRICE_LIMIT_OR_CANCEL = 8
ISTONE_PRICE_TYPE_UNKNOWN = 9
ISTONE_SIDE_BUY = 1
ISTONE_SIDE_SELL = 2
ISTONE_SIDE_PURCHASE = 7
ISTONE_SIDE_REDEMPTION = 8
ISTONE_SIDE_SPLIT = 9
ISTONE_SIDE_MERGE = 10
ISTONE_SIDE_COVER = 11
ISTONE_SIDE_FREEZE = 12
ISTONE_SIDE_SURSTK_TRANS = 27
ISTONE_SIDE_GRTSTK_TRANSIN = 28
ISTONE_SIDE_GRTSTK_TRANSOUT = 29
ISTONE_SIDE_UNKNOWN = 30
ISTONE_POSITION_EFFECT_INIT = 0
ISTONE_POSITION_EFFECT_OPEN = 1
ISTONE_POSITION_EFFECT_CLOSE = 2
ISTONE_POSITION_EFFECT_FORCECLOSE = 3
ISTONE_POSITION_EFFECT_CLOSETODAY = 4
ISTONE_POSITION_EFFECT_CLOSEYESTERDAY = 5
ISTONE_POSITION_EFFECT_FORCEOFF = 6
ISTONE_POSITION_EFFECT_LOCALFORCECLOSE = 7
ISTONE_POSITION_EFFECT_CREDIT_FORCE_COVER = 8
ISTONE_POSITION_EFFECT_CREDIT_FORCE_CLEAR = 9
ISTONE_POSITION_EFFECT_CREDIT_FORCE_DEBT = 10
ISTONE_POSITION_EFFECT_CREDIT_FORCE_UNCOND = 11
ISTONE_POSITION_EFFECT_UNKNOWN = 12
ISTONE_ORDER_ACTION_STATUS_SUBMITTED = 1
ISTONE_ORDER_ACTION_STATUS_ACCEPTED = 2
ISTONE_ORDER_ACTION_STATUS_REJECTED = 3
ISTONE_ORDER_STATUS_INIT = 0
ISTONE_ORDER_STATUS_ALLTRADED = 1
ISTONE_ORDER_STATUS_PARTTRADEDQUEUEING = 2
ISTONE_ORDER_STATUS_PARTTRADEDNOTQUEUEING = 3
ISTONE_ORDER_STATUS_NOTRADEQUEUEING = 4
ISTONE_ORDER_STATUS_CANCELED = 5
ISTONE_ORDER_STATUS_REJECTED = 6
ISTONE_ORDER_STATUS_UNKNOWN = 7
ISTONE_ORDER_SUBMIT_STATUS_INSERT_SUBMITTED = 1
ISTONE_ORDER_SUBMIT_STATUS_INSERT_ACCEPTED = 2
ISTONE_ORDER_SUBMIT_STATUS_INSERT_REJECTED = 3
ISTONE_ORDER_SUBMIT_STATUS_CANCEL_SUBMITTED = 4
ISTONE_ORDER_SUBMIT_STATUS_CANCEL_REJECTED = 5
ISTONE_ORDER_SUBMIT_STATUS_CANCEL_ACCEPTED = 6
ISTONE_TERT_RESTART = 0
ISTONE_TERT_RESUME = 1
ISTONE_TERT_QUICK = 2
ERT_CASH_FORBIDDEN = 0
ERT_CASH_OPTIONAL = 1
ERT_CASH_MUST = 2
ERT_CASH_RECOMPUTE_INTER_SZ = 3
ERT_CASH_MUST_INTER_SZ = 4
ERT_CASH_RECOMPUTE_INTER_OTHER = 5
ERT_CASH_MUST_INTER_OTHER = 6
EPT_INVALID = 7
ISTONE_TICKER_TYPE_SPOT = 1
ISTONE_TICKER_TYPE_INDEX = 2
ISTONE_TICKER_TYPE_OPTION = 4
ISTONE_TICKER_TYPE_UNKNOWN = 5
ISTONE_SECURITY_TYPE_STOCK = 0
ISTONE_SECURITY_TYPE_FUND = 1
ISTONE_SECURITY_TYPE_BOND = 2
ISTONE_SECURITY_TYPE_INDEX = 3
ISTONE_SECURITY_TYPE_OPTION = 4
ISTONE_SECURITY_TYPE_UNKNOWN = 5
ISTONE_BUSINESS_TYPE_CASH = 0
ISTONE_BUSINESS_TYPE_IPOS = 1
ISTONE_BUSINESS_TYPE_REPO = 2
ISTONE_BUSINESS_TYPE_ETF = 3
ISTONE_BUSINESS_TYPE_MARGIN = 4
ISTONE_BUSINESS_TYPE_DESIGNATION = 5
ISTONE_BUSINESS_TYPE_ALLOTMENT = 6
ISTONE_BUSINESS_TYPE_STRUCTURED_FUND_PURCHASE_REDEMPTION = 7
ISTONE_BUSINESS_TYPE_STRUCTURED_FUND_SPLIT_MERGE = 8
ISTONE_BUSINESS_TYPE_MONEY_FUND = 9
ISTONE_BUSINESS_TYPE_OPTION = 10
ISTONE_BUSINESS_TYPE_EXECUTE = 11
ISTONE_BUSINESS_TYPE_FREEZE = 12
ISTONE_BUSINESS_TYPE_UNKNOWN = 13
ISTONE_ACCOUNT_NORMAL = 0
ISTONE_ACCOUNT_CREDIT = 1
ISTONE_ACCOUNT_DERIVE = 2
ISTONE_ACCOUNT_UNKNOWN = 3
ISTONE_FUND_TRANSFER_OUT = 0
ISTONE_FUND_TRANSFER_IN = 1
ISTONE_FUND_INTER_TRANSFER_OUT = 2
ISTONE_FUND_INTER_TRANSFER_IN = 3
ISTONE_FUND_TRANSFER_UNKNOWN = 4
ISTONE_FUND_OPER_PROCESSING = 0
ISTONE_FUND_OPER_SUCCESS = 1
ISTONE_FUND_OPER_FAILED = 2
ISTONE_FUND_OPER_SUBMITTED = 3
ISTONE_FUND_OPER_UNKNOWN = 4
ISTONE_SPLIT_MERGE_STATUS_ALLOW = 0
ISTONE_SPLIT_MERGE_STATUS_ONLY_SPLIT = 1
ISTONE_SPLIT_MERGE_STATUS_ONLY_MERGE = 2
ISTONE_SPLIT_MERGE_STATUS_FORBIDDEN = 3
ISTONE_TBT_ENTRUST = 1
ISTONE_TBT_TRADE = 2
ISTONE_OPT_CALL = 1
ISTONE_OPT_PUT = 2
ISTONE_OPT_EXERCISE_TYPE_EUR = 1
ISTONE_OPT_EXERCISE_TYPE_AME = 2
ISTONE_POSITION_DIRECTION_NET = 0
ISTONE_POSITION_DIRECTION_LONG = 1
ISTONE_POSITION_DIRECTION_SHORT = 2
ISTONE_POSITION_DIRECTION_COVERED = 3
ISTONE_CRD_CR_INIT = 0
ISTONE_CRD_CR_SUCCESS = 1
ISTONE_CRD_CR_FAILED = 2
ISTONE_TRDT_COMMON = '0'
ISTONE_TRDT_CASH = '1'
ISTONE_TRDT_PRIMARY = '2'
ISTONE_TRDT_CROSS_MKT_CASH = '3'
ISTONE_ORDT_Normal = '0'
ISTONE_ORDT_DeriveFromQuote = '1'
ISTONE_ORDT_DeriveFromCombination = '2'
ISTONE_ORDT_Combination = '3'
ISTONE_ORDT_ConditionalOrder = '4'
ISTONE_ORDT_Swap = '5'
ISTONE_EI_SSE = "SSE"
ISTONE_EI_SZSE = "SZSE"
