const utils = require('../utils')

module.exports = {
  users: utils.parseJson('./data/users.json'),
  {{ cookiecutter.model_lower }}: utils.parseJson('./data/{{ cookiecutter.model_lower }}.json'),
}
