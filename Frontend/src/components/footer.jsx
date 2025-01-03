const Footer = () => {
    return (
        <footer className="bg-[#67358E] h-96 md:h-1/3 text-white font-sans">
            {/* Container for logo and social icons */}
            <div className="flex justify-between items-center h-1/2 px-16 py-10">
                {/* Logo Section */}
                <div className="flex items-center">
                    <img
                        src="src/assets/logo-footer.png"
                        alt="Logo"
                        className="h-20 mr-6"
                    />
                </div>

                {/* Social Icons Section */}
                <div className="grid grid-cols-3 md:flex gap-4 items-center ">
                    {[
                        { href: "https://facebook.com", src: "src/assets/icons/facebook.png", alt: "Facebook" },
                        { href: "https://x.com", src: "src/assets/icons/x.png", alt: "X (Twitter)" },
                        { href: "https://instagram.com", src: "src/assets/icons/instagram.png", alt: "Instagram" },
                        { href: "https://youtube.com", src: "src/assets/icons/youtube.png", alt: "YouTube" },
                        { href: "https://tiktok.com", src: "src/assets/icons/tiktok.png", alt: "TikTok" },
                        { href: "https://telegram.org", src: "src/assets/icons/telegram.png", alt: "Telegram" },
                    ].map((icon, index) => (
                        <a
                            key={index}
                            href={icon.href}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="transition-transform transform hover:scale-125"
                        >
                            <img
                                src={icon.src}
                                alt={icon.alt}
                                className="h-16 w-16 rounded-full p-1"
                            />
                        </a>
                    ))}
                </div>
            </div>

            {/* Divider */}
            <hr className="border-t border-white my-5 mx-auto w-11/12" />

            {/* Copyright Section */}
            <div className="flex flex-col md:flex-row justify-center md:justify-between items-center px-4 md:px-16 text-lg space-y-2 md:space-y-0">
                {/* Copyright Line */}
                <p className="text-center md:text-left text-base">
                    Copyright &copy; 2024 chi.ke. All Rights Reserved.
                </p>

                {/* Links Section */}
                <div className="flex justify-center gap-4">
                    <a
                        href="/privacy-policy"
                        className="hover:underline text-base"
                    >
                        Privacy Policy
                    </a>
                    <a
                        href="/terms-of-use"
                        className="hover:underline text-base"
                    >
                        Terms of Use
                    </a>
                </div>
            </div>

        </footer >
    );
};

export default Footer;