import { Factory } from "miragejs"
import { faker } from "@faker-js/faker"

export const {{cookiecutter.model_singular_lower}} = Factory.extend({
  description() {
    return faker.word.verb()
  },
})
