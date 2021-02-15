import win32print
import win32api
import json


status = False
err = {"status": status, "error": ''}

PRINTER_ERROR_STATES = (
    {"ers": win32print.PRINTER_STATUS_NO_TONER,
        "label": 'PRINTER_STATUS_NO_TONER'},
    {"ers": win32print.PRINTER_STATUS_NOT_AVAILABLE,
        "label": 'PRINTER_STATUS_NOT_AVAILABLE'},
    {"ers": win32print.PRINTER_STATUS_OFFLINE, "label": 'PRINTER_STATUS_OFFLINE'},
    {"ers": win32print.PRINTER_STATUS_OUT_OF_MEMORY,
        "label": 'PRINTER_STATUS_OUT_OF_MEMORY'},
    {"ers": win32print.PRINTER_STATUS_OUTPUT_BIN_FULL,
        "label": 'PRINTER_STATUS_OUTPUT_BIN_FULL'},
    {"ers": win32print.PRINTER_STATUS_PAGE_PUNT,
        "label": 'PRINTER_STATUS_PAGE_PUNT'},
    {"ers": win32print.PRINTER_STATUS_PAPER_JAM,
        "label": 'PRINTER_STATUS_PAPER_JAM'},
    {"ers": win32print.PRINTER_STATUS_PAPER_OUT,
        "label": 'PRINTER_STATUS_PAPER_OUT'},
    {"ers": win32print.PRINTER_STATUS_PAPER_PROBLEM,
        "label": 'PRINTER_STATUS_PAPER_PROBLEM'},
)


def printer_errorneous_state(printer, error_states=PRINTER_ERROR_STATES):
    prn_opts = win32print.GetPrinter(printer)
    status_opts = prn_opts[18]
    for error_state in error_states:
        print(status_opts, error_state["ers"])
        if status_opts & error_state["ers"]:
            return error_state
    return 0


def getError(printer_name):
    prn = win32print.OpenPrinter(printer_name)
    error = printer_errorneous_state(prn)
    if error:
        err["status"] = False
        err["error"] = error
    else:
        err["status"] = True
        err["error"] = 'OK'

    win32print.ClosePrinter(prn)
    return err