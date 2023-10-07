import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "D-Jàvue",
  description: "Documentação Oficial do Djàvue",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      //{ text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: 'Documentação',
        items: [
          { text: 'O que é', link: '/intro' },
          { text: 'Instalação', link: '/instalacao' },
          { text: 'Iniciando', link: '/iniciando' },
          { text: 'Contribuindo', link: '/contribuindo' },
          { text: 'CHANGELOG', link: '/changelog' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/evolutio/djavue3' }
    ]
  }
})
