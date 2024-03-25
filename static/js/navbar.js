function toggleMobileMenu() {
  const mobileMenu = document.getElementById("mobile-menu");
  const isExpanded = mobileMenu.className.startsWith("hidden");
  const openMenuIcon = document.getElementById("openMenuIcon");
  const closeMenuIcon = document.getElementById("closeMenuIcon");

  const toggle = document.getElementById("toggleMenuButton");

  mobileMenu.className = isExpanded ? "sm:hidden" : "hidden";
  if (isExpanded) {
    mobileMenu.className = "sm:hidden";
    toggle.setAttribute("aria-expanded", "true");
    closeMenuIcon.classList.replace("hidden", "block");
    openMenuIcon.classList.replace("block", "hidden");
  } else {
    mobileMenu.className = "hidden";
    toggle.setAttribute("aria-expanded", "false");
    openMenuIcon.classList.replace("hidden", "block");
    closeMenuIcon.classList.replace("block", "hidden");
  }
}
