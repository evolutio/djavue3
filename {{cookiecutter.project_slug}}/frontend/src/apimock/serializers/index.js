import { Serializer } from "miragejs"

export const serializers = {
  user: Serializer.extend({
    embed: true,
    root: false,
  }),
}
