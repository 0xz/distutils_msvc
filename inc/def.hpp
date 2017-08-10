

#ifndef _DEF_HPP_
#define _DEF_HPP_

#if defined _WIN32 || defined __CYGWIN__
  #ifdef DLL_EXPORT
    #ifdef __GNUC__
      #define DLL_PUBLISH __attribute__ ((dllexport))
    #else
      #define DLL_PUBLISH __declspec(dllexport)
    #endif
  #else
    #ifdef __GNUC__
      #define DLL_PUBLISH __attribute__ ((dllimport))
    #else
      #define DLL_PUBLISH __declspec(dllimport)
    #endif
  #endif
#else
  #if __GNUC__ >= 4
    #define DLL_PUBLISH __attribute__ ((visibility ("default")))
    #define DLL_PRIVATE __attribute__ ((visibility ("hidden")))
  #endif
#endif

#endif
