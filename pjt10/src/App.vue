<template>
  <div id="app">
		<nav class="py-4 px-7 bg-gray-800">
			<div class="container flex flex-wrap justify-between items-center mx-auto">
				<a href="#" class="flex items-center">
					<router-link class='text-gray-200 self-center text-3xl' :to="{ name: 'home' }">SSAFY Movie</router-link>
				</a>
				<div class="block w-auto" id="mobile-menu">
					<ul class="flex flex-row space-x-8">
						<li>
							<router-link class='text-gray-200 text-xl' :to="{ name: 'home' }">Home</router-link>
						</li>
						<li>
							<router-link class='text-gray-200 text-xl' :to="{ name: 'random' }">Random</router-link>
						</li>
						<li>
							<router-link class='text-gray-200 text-xl' :to="{ name: 'watchList' }">WatchList</router-link>
						</li>
					</ul>
				</div>
			</div>
		</nav>
		<div class="flex flex-row items-center justify-center w-full">
			<router-view />
		</div>
  </div>
</template>
<script>
export default {};
</script>

<style></style>
