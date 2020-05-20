
#---Adding example N3 subdirectories explicitly 
#   and a custom target to for building all example N3 options ----------

cmake_minimum_required(VERSION 2.6 FATAL_ERROR)

add_subdirectory(generation)

add_custom_target(Photon-jet DEPENDS generation)
