
import logging


module_logger = logging.getLogger("main_module.sub_module")  # Hierarchical name


def do_logging():
    module_logger.debug("Submodule debug")
    module_logger.info("Submodule info")
    module_logger.warning("Submodule warning")
    module_logger.error("Submodule error")
    module_logger.critical("Submodule critical")
