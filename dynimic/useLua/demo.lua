function main(splash, args)
    splash:go("http://www.baidu.com")
    splash:wait(0.5)
    local title = splash:evaljs("document.title")
    return {title=title}
end