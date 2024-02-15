import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "D-Jà Vue",
  description: "Documentação Oficial do Djàvue",
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
          { text: '📦 Gerenc.Pacotes', link: '/05-gerenc-pacotes' },
          { text: '🗂️ Organização', link: '/06-organizacao' },
          { text: '🐞 Debug', link: '/07-debug' },
          { text: '🤡 API Mock', link: '/08-api-mock' },
          { text: '🚀 Deploy', link: '/09-deploy' },
          { text: '🌀 CI & CD', link: '/10-CI-e-CD' },
          { text: '👾 Contribuindo', link: '/11-contribuindo' },
          { text: '📝 CHANGELOG', link: '/changelog' },
          { text: '🇬🇧 English', link: '/README_EN' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/evolutio/djavue3' },
      { icon: 'youtube', link: 'https://www.youtube.com/watch?v=pDYvJIxxoN0&list=PL1Skk6O-pP7vRPCWmzMYXNEkx4BMZlhgi' }
    ]
  }
})
