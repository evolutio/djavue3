import { accounts } from "./accounts"
import {%raw%}{{%endraw%} {{cookiecutter.app_name}} {%raw%}}{%endraw%} from "./{{cookiecutter.app_name}}"

export const routes = function () {
  accounts(this), {{cookiecutter.app_name}}(this)
}
