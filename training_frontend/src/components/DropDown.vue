<template>
  <div class="dropdown-wrapper relative m-8">
    <button
      v-on:click="show = !show"
      class="
        text-white
        font-bold
        py-2
        px-4
        whitespace-no-wrap
        rounded
        transition
        duration-300
      "
    >
      Dropdown <i class="fas fa-chevron-down ml-2"></i>
    </button>
    <transition :name="animation">
      <div
        class="
          dropdown-menu
          text-white
          mt-1
          rounded
          absolute
          z-10
          shadow-lg
          w-40
          max-w-xs
        "
        v-if="show"
      >
        <ul class="list-none overflow-hidden rounded">
          <li v-for="car in cars">
            <a href="" class="flex py-2 px-4 transition duration-300">{{
              car
            }}</a>
          </li>
        </ul>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: false,
      cars: ["BMW", "Mercedes", "Audi", "Volvo"],
    };
  },
  props: {
    color: String,
    animation: String,
  },
};
</script>
    



<style>
/* Animations */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

/* Slide-in-up animation*/
.slide-in-up-enter-active,
.slide-in-up-leave-active {
  transition: all 0.5s;
  transform: translateY(0);
}
.slide-in-up-enter,
.slide-in-up-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

/* Slide-in-right animation*/
.slide-in-right-enter-active,
.slide-in-right-leave-active {
  transition: all 0.5s;
  transform: translateX(0);
}
.slide-in-right-enter,
.slide-in-right-leave-to {
  opacity: 0;
  transform: translateX(20px);
}

/* Slide-in-left animation*/
.slide-in-left-enter-active,
.slide-in-left-leave-active {
  transition: all 0.5s;
  transform: translateX(0);
}
.slide-in-left-enter,
.slide-in-left-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}

/* Scale animation*/
.scale-enter-active,
.scale-leave-active {
  transition: all 0.5s;
  transform: scale(1);
}
.scale-enter,
.scale-leave-to {
  opacity: 0;
  transform: scale(0);
}

/* Rotate animation*/
.rotate-enter-active,
.rotate-leave-active {
  transition: all 0.5s;
  transform: scale(1) rotate(-360deg);
}
.rotate-enter,
.rotate-leave-to {
  opacity: 0;
  transform: scale(0) rotate(360deg);
}
</style>