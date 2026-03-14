/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			colors: {
				journal: {
					bg: '#F9F7F2',
					text: '#080808',
					accent: '#9B1B30',
					faded: '#666666',
					// High contrast colors
					green: '#004d40', 
					blue: '#001f3f', 
					gold: '#856404',
					tan: '#ede0d4',
				}
			},
			fontFamily: {
				serif: ['"Libre Baskerville"', 'serif'],
				sans: ['Inter', 'sans-serif'],
				urdu: ['"Jameel Noori Nastaleeq"', '"Noto Nastaliq Urdu"', 'serif'],
			},
		},
	},
	plugins: [],
}
