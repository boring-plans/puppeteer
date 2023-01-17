<script setup>
import { ref } from 'vue';

const toolbarPos = ref([50, 50]);
const startPos = ref([]);
const containerRef = ref(null);
const BASE_URL = 'http://192.168.9.108:5000/';

function triggerEvent(event, data) {
  fetch(BASE_URL + event, { method: 'put', headers: { 'Content-Type': 'application/json;charset=utf-8' }, body: JSON.stringify(data) });
}

function getRelativePos(ev) {
  if (containerRef.value) {
    const { offsetX, offsetY } = ev;
    startPos.value = [offsetX, offsetY];
    const { offsetWidth, offsetHeight } = containerRef.value;
    return [offsetX / offsetWidth, offsetY / offsetHeight];
  }
  return [0, 0];
}

function mousemove(ev) {
  triggerEvent('mouseto-event', { pos: getRelativePos(ev) });
}

function mouseup(ev) {
  startPos.value = [];
  window.removeEventListener('mouseup', mouseup);
  window.removeEventListener('mousemove', mousemove);

  triggerEvent('mouseup-event', { pos: getRelativePos(ev) });
}

function mousedown(ev) {
  window.addEventListener('mouseup', mouseup);
  window.addEventListener('mousemove', mousemove);

  triggerEvent('mousedown-event', { pos: getRelativePos(ev) });
}
</script>

<template>
  <main ref="containerRef">
    <img
      :src="BASE_URL+'/frame'"
      class="player"
      @mousedown="mousedown"
    />
    <div class="toolbar" :style="{top: toolbarPos[1]+'px', left: toolbarPos[0]+'px'}">1</div>
  </main>
</template>

<style scoped>
main {
  margin: auto;
  position: relative;
  height: 100%;
  width: 100%;
}

.player {
  object-fit: contain;
  user-select: none;
  display: block;
  height: 100%;
  width: 100%;
}

.toolbar {
  position: absolute;
  width: 10vw;
  color: white;
  background: rgba(0, 0, 0, .37);
  backdrop-filter: saturate(180%) blur(20px);
  padding: 24px;
  border-radius: 12px;
  cursor: pointer;
}
</style>
