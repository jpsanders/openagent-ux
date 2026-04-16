#!/usr/bin/env node
/**
 * OpenAgent UX - Initialization
 * 
 * Run after: git clone + npm install
 * Usage: node scripts/init.js
 *        OR: npm run init
 * 
 * This script launches the user's agent (OpenCode by default) with a 
 * questionnaire prompt to configure their project.
 */

const { spawn } = require('child_process');
const readline = require('readline');
const path = require('path');
const fs = require('fs');

const CONFIG_FILE = '.openagent-ux.json';
const DEFAULT_AGENT = 'opencode';

// Question categories for the questionnaire
const QUESTIONS = {
  architecture: [
    {
      key: 'projectType',
      question: 'What type of project are you building?',
      options: ['SaaS application', 'Marketing website', 'Blog / Content site', 'Portfolio', 'E-commerce store', 'Documentation site', 'Dashboard / Admin', 'Other']
    },
    {
      key: 'projectName',
      question: 'What is your project name?',
      type: 'text'
    },
    {
      key: 'description',
      question: 'Briefly describe your project:',
      type: 'text'
    }
  ],
  
  techstack: [
    {
      key: 'framework',
      question: 'Which framework do you want to use?',
      options: ['Astro', 'Next.js', 'Gatsby', 'Nuxt', 'Hugo', 'HTML (vanilla)', 'React (Vite)']
    },
    {
      key: 'language',
      question: 'Preferred language?',
      options: ['TypeScript', 'JavaScript']
    },
    {
      key: 'styling',
      question: 'Which styling approach?',
      options: ['Tailwind CSS', 'CSS Modules', 'Styled Components', 'Plain CSS', 'Sass/SCSS']
    }
  ],
  
  design: [
    {
      key: 'personality',
      question: 'Choose a design personality (defines typography, colors, spacing):',
      options: [
        'Swiss - High contrast, precise, functional',
        'Editorial - Sophisticated, timeless',
        'Tech Noir - Dark, technical, futuristic',
        'Playful - Friendly, bouncy, creative',
        'Minimal - Essential, reductionist',
        'Contemporary - Bold, expressive, modern'
      ]
    },
    {
      key: 'colors',
      question: 'Do you have brand colors?',
      type: 'text',
      placeholder: 'Enter hex codes or color names (optional)'
    },
    {
      key: 'typography',
      question: 'Any typography preferences?',
      type: 'text',
      placeholder: 'Font names or categories (optional)'
    },
    {
      key: 'motion',
      question: 'Motion preference?',
      options: ['Subtle (minimal animations)', 'Standard (typical web animations)', 'Playful (bouncy, engaging)', 'None (static)']
    }
  ],
  
  frontend: {
    pages: [
      {
        key: 'requiredPages',
        question: 'Which pages do you need? (select all that apply)',
        multi: true,
        options: ['Home', 'About', 'Contact', 'Blog', 'Pricing', 'Portfolio', 'Shop/Products', 'Dashboard', 'Login/Register', 'Documentation']
      }
    ],
    components: [
      {
        key: 'heroStyle',
        question: 'Hero section style?',
        options: ['Full-width image/video', 'Split (text + image)', 'Centered text', 'Minimal/Text-only', 'Interactive/Animated']
      },
      {
        key: 'navigation',
        question: 'Navigation type?',
        options: ['Standard navbar', 'Mega menu', 'Sidebar navigation', 'Floating/Sticky', 'None (single page)']
      },
      {
        key: 'footer',
        question: 'Footer style?',
        options: ['Multi-column (rich)', 'Simple (links only)', 'Minimal', 'None']
      }
    ]
  },
  
  backend: [
    {
      key: 'auth',
      question: 'Authentication needs?',
      options: ['None needed', 'User login/signup', 'Social login (OAuth)', 'Admin dashboard with auth']
    },
    {
      key: 'database',
      question: 'Database requirements?',
      options: ['None (static site)', 'SQL database (PostgreSQL/MySQL)', 'NoSQL (MongoDB)', 'Edge database (D1/Supabase)', 'CMS as backend']
    },
    {
      key: 'api',
      question: 'Custom API needs?',
      options: ['None', 'REST API', 'GraphQL', 'Real-time (WebSockets)']
    },
    {
      key: 'hosting',
      question: 'Preferred hosting?',
      options: ['Vercel', 'Netlify', 'Cloudflare Pages', 'Node.js server', 'Static hosting']
    }
  ],
  
  pickAndMix: {
    instructions: `
╔══════════════════════════════════════════════════════════════════════════════╗
║                          PICK N' MIX SELECTION                                ║
║                                                                               ║
║  Now comes the unique part! You can mix and match components from           ║
║  50+ pre-built templates to create something truly unique.                  ║
║                                                                               ║
║  Browse available components at: templates/ and components/                 ║
║  Or check the registry: components-registry.json                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
`,
    sections: [
      {
        key: 'heroComponents',
        question: 'Pick a hero component style:',
        options: ['From astrowind - SaaS marketing hero', 'From astroship - Startup hero', 'From nextjs-dashboard - Clean admin hero', 'Create custom']
      },
      {
        key: 'buttonComponents',
        question: 'Pick a button style:',
        options: ['From shadcn-ui', 'From daisyui', 'From mantine', 'From custom design system']
      },
      {
        key: 'cardComponents',
        question: 'Pick a card style:',
        options: ['From gatsby-portfolio-cara', 'From nextjs-commerce', 'From astro-paper', 'Create custom']
      },
      {
        key: 'navbarComponents',
        question: 'Pick a navbar style:',
        options: ['From astrowind', 'From starlight-docs', 'From gatsby-starter-blog', 'Create custom']
      },
      {
        key: 'footerComponents',
        question: 'Pick a footer style:',
        options: ['From astrowind (multi-column)', 'From hugo-universal', 'From nextjs-commerce', 'Create custom']
      }
    ]
  }
};

class InitCLI {
  constructor() {
    this.config = {};
    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
  }

  async ask(question) {
    return new Promise((resolve) => {
      this.rl.question(question + '\n> ', (answer) => {
        resolve(answer);
      });
    });
  }

  async askOption(question, options) {
    console.log(`\n${question}\n`);
    options.forEach((opt, i) => {
      console.log(`  ${i + 1}. ${opt}`);
    });
    console.log('');
    
    const answer = await this.ask('Enter number (or press Enter for default)');
    const num = parseInt(answer);
    
    if (num >= 1 && num <= options.length) {
      return options[num - 1];
    }
    return options[0]; // Default
  }

  async askMultiOption(question, options) {
    console.log(`\n${question}\n`);
    console.log('  Enter numbers separated by commas (e.g., 1,3,5)');
    console.log('  Or press Enter for none\n');
    options.forEach((opt, i) => {
      console.log(`  ${i + 1}. ${opt}`);
    });
    console.log('');
    
    const answer = await this.ask('Select options');
    
    if (!answer.trim()) {
      return [];
    }
    
    return answer
      .split(',')
      .map(s => parseInt(s.trim()))
      .filter(n => n >= 1 && n <= options.length)
      .map(n => options[n - 1]);
  }

  async runQuestionnaire() {
    console.clear();
    console.log(`
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗  ██████╗  ███████╗ █████╗ ████████╗███████╗██╗  ██╗               ║
║   ██╔══██╗██╔═══██╗ ██╔════╝██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝               ║
║   ██████╔╝██║   ██║ █████╗  ███████║   ██║   █████╗   ╚███╔╝                ║
║   ██╔══██╗██║   ██║ ██╔══╝  ██╔══██║   ██║   ██╔══╝   ██╔██╗                ║
║   ██████╔╝╚██████╔╝ ███████╗██║  ██║   ██║   ███████╗██╔╝ ██╗               ║
║   ╚═════╝  ╚═════╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝               ║
║                                                                              ║
║   ███████╗ ██████╗ ██████╗  ███████╗ █████╗  ██████╗ ██╗  ██╗               ║
║   ██╔════╝██╔═══██╗██╔══██╗ ██╔════╝██╔══██╗██╔════╝ ██║  ██║               ║
║   ███████╗██║   ██║██████╔╝ █████╗  ███████║██║  ███╗███████║               ║
║   ╚════██║██║   ██║██╔══██╗ ██╔══╝  ██╔══██║██║   ██║╚════██║               ║
║   ███████║╚██████╔╝██║  ██║ ███████╗██║  ██║╚██████╔╝ ███████║               ║
║   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══════╝               ║
║                                                                              ║
║   Welcome! This questionnaire will help configure your project.             ║
║   Your selections will be saved and passed to the AI agent.                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
`);

    console.log('\nPress Ctrl+C to cancel at any time.\n');
    await this.ask('Press Enter to begin...');

    // Architecture
    console.log('\n' + '='.repeat(70));
    console.log('1. ARCHITECTURE');
    console.log('='.repeat(70));
    
    for (const q of QUESTIONS.architecture) {
      if (q.options) {
        this.config[q.key] = await this.askOption(q.question, q.options);
      } else {
        this.config[q.key] = await this.ask(q.question + (q.placeholder ? ` (${q.placeholder})` : ''));
      }
    }

    // Tech Stack
    console.log('\n' + '='.repeat(70));
    console.log('2. TECH STACK');
    console.log('='.repeat(70));
    
    for (const q of QUESTIONS.techstack) {
      if (q.options) {
        this.config[q.key] = await this.askOption(q.question, q.options);
      } else {
        this.config[q.key] = await this.ask(q.question);
      }
    }

    // Design
    console.log('\n' + '='.repeat(70));
    console.log('3. DESIGN');
    console.log('='.repeat(70));
    
    for (const q of QUESTIONS.design) {
      if (q.options) {
        this.config[q.key] = await this.askOption(q.question, q.options);
      } else {
        this.config[q.key] = await this.ask(q.question + (q.placeholder ? ` (${q.placeholder})` : ''));
      }
    }

    // Frontend - Pages
    console.log('\n' + '='.repeat(70));
    console.log('4. FRONTEND - PAGES');
    console.log('='.repeat(70));
    
    for (const q of QUESTIONS.frontend.pages) {
      if (q.multi) {
        this.config[q.key] = await this.askMultiOption(q.question, q.options);
      } else {
        this.config[q.key] = await this.askOption(q.question, q.options);
      }
    }

    // Frontend - Components
    console.log('\n' + '='.repeat(70));
    console.log('5. FRONTEND - COMPONENTS');
    console.log('='.repeat(70));
    
    for (const q of QUESTIONS.frontend.components) {
      this.config[q.key] = await this.askOption(q.question, q.options);
    }

    // Backend
    console.log('\n' + '='.repeat(70));
    console.log('6. BACKEND');
    console.log('='.repeat(70));
    
    for (const q of QUESTIONS.backend) {
      this.config[q.key] = await this.askOption(q.question, q.options);
    }

    // Pick n' Mix
    console.log('\n' + QUESTIONS.pickAndMix.instructions);
    
    for (const q of QUESTIONS.pickAndMix.sections) {
      this.config[q.key] = await this.askOption(q.question, q.options);
    }

    // Save config
    this.saveConfig();

    // Launch agent
    await this.launchAgent();
  }

  saveConfig() {
    const configPath = path.join(process.cwd(), CONFIG_FILE);
    fs.writeFileSync(configPath, JSON.stringify(this.config, null, 2));
    console.log(`\n✓ Configuration saved to ${CONFIG_FILE}`);
  }

  async launchAgent() {
    console.log('\n' + '='.repeat(70));
    console.log('CONFIGURATION COMPLETE');
    console.log('='.repeat(70));
    
    console.log('\nNow launching AI agent with your configuration...');
    console.log('The agent will orchestrate the build based on your answers.\n');

    const agent = process.env.OPENCODE_AGENT || DEFAULT_AGENT;
    
    // Build prompt for the agent
    const prompt = this.buildAgentPrompt();
    
    // Launch the agent with the prompt
    console.log(`Starting ${agent} with your project configuration...\n`);
    
    const child = spawn(agent, ['--prompt', prompt], {
      stdio: 'inherit',
      shell: true,
      cwd: process.cwd()
    });

    child.on('exit', (code) => {
      console.log(`\nAgent exited with code ${code}`);
      this.rl.close();
      process.exit(code);
    });
  }

  buildAgentPrompt() {
    const cfg = this.config;
    
    return `
# OpenAgent UX - Project Initialization

## Project Configuration

### Architecture
- **Project Type**: ${cfg.projectType}
- **Project Name**: ${cfg.projectName}
- **Description**: ${cfg.description}

### Tech Stack
- **Framework**: ${cfg.framework}
- **Language**: ${cfg.language}
- **Styling**: ${cfg.styling}

### Design
- **Personality**: ${cfg.personality}
- **Colors**: ${cfg.colors || 'Not specified'}
- **Typography**: ${cfg.typography || 'Not specified'}
- **Motion**: ${cfg.motion}

### Frontend - Pages
- **Required Pages**: ${(cfg.requiredPages || []).join(', ')}

### Frontend - Components
- **Hero Style**: ${cfg.heroStyle}
- **Navigation**: ${cfg.navigation}
- **Footer**: ${cfg.footer}

### Backend
- **Authentication**: ${cfg.auth}
- **Database**: ${cfg.database}
- **API**: ${cfg.api}
- **Hosting**: ${cfg.hosting}

### Pick n' Mix Components
- **Hero**: ${cfg.heroComponents}
- **Buttons**: ${cfg.buttonComponents}
- **Cards**: ${cfg.cardComponents}
- **Navbar**: ${cfg.navbarComponents}
- **Footer**: ${cfg.footerComponents}

---

## Your Task

You are the Principal Architect agent. Based on the configuration above:

1. **Analyze** the requirements and create a project plan
2. **Delegate** to domain leads (Design Lead, Frontend Lead, Backend Lead, QA Lead)
3. **Orchestrate** the build using the multi-agent system
4. **Assemble** the site using the pick n' mix components from the template library

Available templates are in: templates/
Available components are in: components/
Component registry: components-registry.json
Design systems: design-systems/

Start by creating an execution plan, then delegate to the appropriate leads.

IMPORTANT: Use the pre-built templates and components as much as possible to avoid AI-generated generic code. The pick n' mix selection should guide component choices.
`;
  }
}

// Main execution
const cli = new InitCLI();

process.on('SIGINT', () => {
  console.log('\n\nInitialization cancelled.');
  cli.rl.close();
  process.exit(1);
});

cli.runQuestionnaire().catch(err => {
  console.error('Error:', err);
  cli.rl.close();
  process.exit(1);
});