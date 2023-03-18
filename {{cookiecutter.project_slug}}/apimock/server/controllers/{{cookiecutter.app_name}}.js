const data = require("../data");
const accounts = require("./accounts");

function getMaxId(items) {
  return Math.max(...items.map((item) => item.id));
}

module.exports = {
  find: (req, res) => {
    const loggedUser = accounts.loginRequired(req, res);
    if (!loggedUser) {
      return;
    }
    const { id } = req.params;
    if (id != undefined) {
      const {{cookiecutter.model_singular_lower}} = data.{{ cookiecutter.model_lower }}.find((t) => t.id == id);
      if (!{{cookiecutter.model_singular_lower}} || {{cookiecutter.model_singular_lower}}.userId != loggedUser.id) {
        res.status(404).end();
        return;
      }
      res.send({{cookiecutter.model_singular_lower}});
      return;
    }
    const response = {
      {{cookiecutter.model_lower}}: data.{{ cookiecutter.model_lower }}.filter((t) => t.userId == loggedUser.id),
    };
    res.send(response);
  },
  add: (req, res) => {
    const loggedUser = accounts.loginRequired(req, res);
    if (!loggedUser) {
      return;
    }
    const { description } = req.body;
    const id = getMaxId(data.{{ cookiecutter.model_lower }}) + 1;
    const new{{cookiecutter.model_singular}} = {
      id,
      description,
      userId: loggedUser.id,
    };
    data.{{ cookiecutter.model_lower }}.push(new{{cookiecutter.model_singular}});
    res.send(new{{cookiecutter.model_singular}});
  },
};
