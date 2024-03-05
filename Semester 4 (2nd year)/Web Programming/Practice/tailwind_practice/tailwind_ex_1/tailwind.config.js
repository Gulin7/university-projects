/** @type {import('tailwindcss').Config} */
module.exports = {
	mode: 'jit',
	purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
	content: ['./dist/*.{html,js}'],
	theme: {
		container: {
			center: true,
			padding: '4rem',
		},
	},
	plugins: [],
}
