<?php
/**
 * Displays an HTML page of the scoreboard by calling a python script.
 */
$root = "/var/www/html/scoreboard";
print shell_exec(escapeshellcmd("python $root/scoreboard.py"));
