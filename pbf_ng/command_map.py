from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig("new ng-module", "pbf_ng.Commands.new_module.NewModule", description="Create a new Angular Module")]

RegisterCommands(commands)