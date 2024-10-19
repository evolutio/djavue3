import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "D-Jà Vue",
  description: "Documentação Oficial do Djàvue",
  locales: {
    root: {
      label: 'Português',
      lang: 'pt-br',
      themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        nav: [
          { text: 'Home', link: '/' },
          //{ text: 'Examples', link: '/markdown-examples' }
        ],

        sidebar: [
          {
            text: 'Documentação 🇧🇷',
            items: [
              { text: '🤔 O que é', link: '/01-o-que-eh' },
              { text: '💿 Iniciando', link: '/02-iniciando' },
              { text: '📦 Sem Docker', link: '/03-sem-docker' },
              { text: '🐋 Com Docker', link: '/04-com-docker' },
              { text: '📦 Gerenciador de pacotes', link: '/05-gerenc-pacotes' },
              { text: '🗂️ Organização', link: '/06-organizacao' },
              { text: '🐞 Debug', link: '/07-debug' },
              { text: '🤡 API Mock', link: '/08-api-mock' },
              { text: '🚀 Deploy', link: '/09-deploy' },
              { text: '🌀 CI & CD', link: '/10-CI-e-CD' },
              { text: '👾 Contribuindo', link: '/11-contribuindo' },
              { text: '📝 CHANGELOG', link: '/changelog' },
            ]
          }
        ],

        socialLinks: [
          { icon: 'github', link: 'https://github.com/evolutio/djavue3' },
          { icon: 'youtube', link: 'https://www.youtube.com/watch?v=zO8M7f7L1fQ&list=PL1Skk6O-pP7vRPCWmzMYXNEkx4BMZlhgi' },
          { icon: 'facebook', link: 'https://t.me/+5eC434i4iNAxZDUx'},
          { icon: 'x', link: 'https://x.com/huogerac'},
        ]
      }
    },
    en: {
      label: 'English',
      lang: 'en',
      link: '/en',
      themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        nav: [
          { text: 'Home', link: 'en/index.md' },
          //{ text: 'Examples', link: '/markdown-examples' }
        ],

        sidebar: [
          {
            text: 'Documentation 🇺🇸',
            items: [
              { text: '🤔 Introduction', link: '/en/01-o-que-eh' },
              { text: '💿 Initializing', link: '/en/02-iniciando' },
              { text: '📦 Without Docker', link: '/en/03-sem-docker' },
              { text: '🐋 With Docker', link: '/en/04-com-docker' },
              { text: '📦 Package management', link: '/en/05-gerenc-pacotes' },
              { text: '🗂️ Organization', link: '/en/06-organizacao' },
              { text: '🐞 Debug', link: '/en/07-debug' },
              { text: '🤡 API Mock', link: '/en/08-api-mock' },
              { text: '🚀 Deploy', link: '/en/09-deploy' },
              { text: '🌀 CI & CD', link: '/en/10-CI-e-CD' },
              { text: '👾 Contributing', link: '/en/11-contribuindo' },
              { text: '📝 CHANGELOG', link: '/en/changelog' },
            ]
          }
        ],

        socialLinks: [
          { icon: 'github', link: 'https://github.com/evolutio/djavue3' },
          { icon: 'youtube', link: 'https://www.youtube.com/watch?v=zO8M7f7L1fQ&list=PL1Skk6O-pP7vRPCWmzMYXNEkx4BMZlhgi' },
          { icon: 'facebook', link: 'https://t.me/+5eC434i4iNAxZDUx'},
          { icon: 'x', link: 'https://x.com/huogerac'},
        ]
      }
    }
  },
})
